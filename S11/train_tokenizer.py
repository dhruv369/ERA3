from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors
import json
import os

def create_bpe_tokenizer():
    """Initialize a BPE tokenizer"""
    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
    tokenizer.decoder = decoders.ByteLevel()
    return tokenizer

def calculate_compression_ratio(tokenizer, text):
    """Calculate compression ratio for given text"""
    encoding = tokenizer.encode(text)
    original_length = len(text)
    tokenized_length = len(encoding.tokens)
    return original_length / tokenized_length if tokenized_length > 0 else 0

def train_tokenizer(data_path, vocab_size=4500, min_frequency=2):
    """Train the tokenizer on the given dataset"""
    tokenizer = create_bpe_tokenizer()
    
    # Define special tokens
    special_tokens = ["<unk>", "<pad>", "<bos>", "<eos>"]
    
    # Configure trainer with optimized parameters
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=special_tokens,
        min_frequency=min_frequency,
        show_progress=True,
        initial_alphabet=[],
        continuing_subword_prefix="##",
        end_of_word_suffix="</w>"
    )
    
    def load_dataset(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
        augmented_data = []
        
        # Process lines in groups of related content
        for i in range(len(lines)):
            current_line = lines[i]
            words = current_line.split()
            
            # Add original line
            augmented_data.append(current_line)
            
            # Add bigrams and trigrams
            if len(words) > 2:
                for j in range(len(words)-1):
                    augmented_data.append(f"{words[j]} {words[j+1]}")
                    if j < len(words)-2:
                        augmented_data.append(f"{words[j]} {words[j+1]} {words[j+2]}")
            
            # Add reversed sentence for pattern learning
            augmented_data.append(" ".join(words[::-1]))
            
            # Combine with next sentence if available
            if i < len(lines) - 1:
                next_line = lines[i + 1]
                augmented_data.append(f"{current_line} {next_line}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_data = []
        for item in augmented_data:
            if item not in seen:
                seen.add(item)
                unique_data.append(item)
        
        return unique_data
    
    # Train the tokenizer
    training_data = load_dataset(data_path)
    tokenizer.train_from_iterator(training_data, trainer)
    
    # Add post-processor
    tokenizer.post_processor = processors.TemplateProcessing(
        single="<bos> $A <eos>",
        special_tokens=[("<bos>", 2), ("<eos>", 3)]
    )
    
    return tokenizer, training_data

def evaluate_tokenizer(tokenizer, training_data):
    """Evaluate tokenizer performance"""
    # Calculate vocabulary size
    vocab = tokenizer.get_vocab()
    vocab_size = len(vocab)
    print(f"Vocabulary Size: {vocab_size}")
    
    # Print vocabulary details
    print("\nVocabulary Preview (first 20 tokens):")
    sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])
    for token, id in sorted_vocab[:20]:
        print(f"Token: {token:20} ID: {id}")
    
    print(f"\nSpecial Tokens:")
    special_tokens = ["<unk>", "<pad>", "<bos>", "<eos>"]
    for token in special_tokens:
        if token in vocab:
            print(f"Token: {token:20} ID: {vocab[token]}")
    
    # Calculate average compression ratio across all training data
    compression_ratios = []
    for text in training_data:
        ratio = calculate_compression_ratio(tokenizer, text)
        compression_ratios.append(ratio)
    
    avg_compression_ratio = sum(compression_ratios) / len(compression_ratios)
    print(f"\nAverage Compression Ratio: {avg_compression_ratio:.2f}")
    
    # Print sample tokenization
    sample_text = training_data[0]
    print("\nSample Tokenization:")
    print(f"Original text: {sample_text}")
    print(f"Tokens: {tokenizer.encode(sample_text).tokens}")
    
    return vocab_size, avg_compression_ratio

def main():
    # Configuration
    DATA_PATH = "example_data.txt"
    SAVE_PATH = "bpe_tokenizer.json"
    VOCAB_SIZE = 4500  # Target size with margin for safety
    MIN_FREQUENCY = 2
    MIN_COMPRESSION_RATIO = 3.2
    
    print("Starting tokenizer training...")
    
    # Train tokenizer
    tokenizer, training_data = train_tokenizer(
        data_path=DATA_PATH,
        vocab_size=VOCAB_SIZE,
        min_frequency=MIN_FREQUENCY
    )
    
    # Evaluate tokenizer
    print("\nEvaluating tokenizer...")
    vocab_size, compression_ratio = evaluate_tokenizer(tokenizer, training_data)
    
    # Check requirements and show warnings
    if vocab_size >= 5000:
        print(f"\nWarning: Vocabulary size ({vocab_size}) exceeds 5000 tokens!")
    
    if compression_ratio < 3.2:
        print(f"\nWarning: Compression ratio ({compression_ratio:.2f}) is below 3.2!")
    
    # Save tokenizer regardless of requirements
    tokenizer.save(SAVE_PATH)
    print(f"\nTokenizer saved to {SAVE_PATH}")
    print(f"Final Vocabulary Size: {vocab_size}")
    print(f"Final Compression Ratio: {compression_ratio:.2f}")
    
    # Print recommendations if requirements weren't met
    if vocab_size >= 5000 or compression_ratio < 3.2:
        print("\nRecommendations for improvement:")
        if vocab_size >= 5000:
            print("- To reduce vocabulary size: Increase min_frequency or decrease vocab_size parameter")
        if compression_ratio < 3.2:
            print("- To improve compression ratio: Add more repetitive patterns to training data")
            print("- Consider adding more examples with common phrases and sentence structures")
    
    print("\nTraining completed!")

if __name__ == "__main__":
    main() 