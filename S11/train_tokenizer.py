from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors
import json
import os

def create_bpe_tokenizer():
    """Initialize a BPE tokenizer"""
    tokenizer = Tokenizer(models.BPE())
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
    tokenizer.decoder = decoders.ByteLevel()
    return tokenizer

def train_tokenizer(data_path, vocab_size=5000, min_frequency=2):
    """Train the tokenizer on the given dataset"""
    # Initialize tokenizer
    tokenizer = create_bpe_tokenizer()
    
    # Define special tokens
    special_tokens = ["<unk>", "<pad>", "<bos>", "<eos>"]
    
    # Configure trainer
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        special_tokens=special_tokens,
        min_frequency=min_frequency
    )
    
    # Load and preprocess training data
    def load_dataset(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    
    # Train the tokenizer
    training_data = load_dataset(data_path)
    tokenizer.train_from_iterator(training_data, trainer)
    
    # Add post-processor for special tokens
    tokenizer.post_processor = processors.TemplateProcessing(
        single="<bos> $A <eos>",
        special_tokens=[("<bos>", 2), ("<eos>", 3)]
    )
    
    return tokenizer

def evaluate_tokenizer(tokenizer, test_text):
    """Evaluate tokenizer performance"""
    # Calculate vocabulary size
    vocab_size = len(tokenizer.get_vocab())
    print(f"Vocabulary Size: {vocab_size}")
    
    # Calculate compression ratio
    encoding = tokenizer.encode(test_text)
    original_length = len(test_text)
    tokenized_length = len(encoding.tokens)
    compression_ratio = original_length / tokenized_length
    print(f"Compression Ratio: {compression_ratio:.2f}")
    
    # Print sample tokenization
    print("\nSample Tokenization:")
    print(f"Original text: {test_text}")
    print(f"Tokens: {encoding.tokens}")
    
    return vocab_size, compression_ratio

def main():
    # Configuration
    DATA_PATH = "example_data.txt"
    SAVE_PATH = "bpe_tokenizer.json"
    VOCAB_SIZE = 5000
    MIN_FREQUENCY = 2
    
    print("Starting tokenizer training...")
    
    # Train tokenizer
    tokenizer = train_tokenizer(
        data_path=DATA_PATH,
        vocab_size=VOCAB_SIZE,
        min_frequency=MIN_FREQUENCY
    )
    
    # Save tokenizer
    tokenizer.save(SAVE_PATH)
    print(f"\nTokenizer saved to {SAVE_PATH}")
    
    # Evaluate on sample text
    print("\nEvaluating tokenizer...")
    sample_text = "नमस्ते भारत! यह एक उदाहरण पाठ है।"
    vocab_size, compression_ratio = evaluate_tokenizer(tokenizer, sample_text)
    
    # Validate requirements
    if vocab_size > 5000:
        print("\nWarning: Vocabulary size exceeds 5000 tokens!")
    if compression_ratio < 3.2:
        print("\nWarning: Compression ratio is below 3.2!")
    
    print("\nTraining completed!")

if __name__ == "__main__":
    main() 