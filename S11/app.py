import gradio as gr
from tokenizers import Tokenizer
import json

# Load the tokenizer
tokenizer = Tokenizer.from_file("bpe_tokenizer.json")

def tokenize_text(text):
    """Tokenize input text and return tokens with statistics"""
    encoding = tokenizer.encode(text)
    tokens = encoding.tokens
    
    # Calculate statistics
    original_length = len(text)
    tokenized_length = len(tokens)
    compression_ratio = original_length / tokenized_length
    
    # Format output
    result = f"Tokens: {tokens}\n\n"
    result += f"Statistics:\n"
    result += f"Original Length: {original_length}\n"
    result += f"Number of Tokens: {tokenized_length}\n"
    result += f"Compression Ratio: {compression_ratio:.2f}"
    
    return result

# Create Gradio interface
iface = gr.Interface(
    fn=tokenize_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter Hindi text here..."),
    outputs=gr.Textbox(lines=8),
    title="Hindi BPE Tokenizer",
    description="This tokenizer implements Byte Pair Encoding for Hindi text with a vocabulary size < 5000 tokens."
)

if __name__ == "__main__":
    iface.launch() 