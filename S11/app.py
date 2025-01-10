import streamlit as st
import os

# Handle tokenizers import
try:
    from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers
except ImportError:
    st.error("Error: Could not import tokenizers. Installing required packages...")
    os.system("pip install tokenizers==0.15.1")
    from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers

import json

# Page configuration
st.set_page_config(
    page_title="Hindi BPE Tokenizer",
    page_icon="🤖",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .output-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize tokenizer with error handling
@st.cache_resource
def load_tokenizer():
    try:
        if os.path.exists("bpe_tokenizer.json"):
            return Tokenizer.from_file("bpe_tokenizer.json")
        else:
            st.warning("Creating a new BPE tokenizer...")
            # Create a new BPE tokenizer
            tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
            tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
            tokenizer.decoder = decoders.ByteLevel()
            
            # Add special tokens
            special_tokens = ["<unk>", "<pad>", "<bos>", "<eos>"]
            trainer = trainers.BpeTrainer(
                vocab_size=4500,
                special_tokens=special_tokens,
                min_frequency=2
            )
            
            # Train on some basic Hindi text
            basic_texts = [
                "नमस्ते भारत! यह एक उदाहरण पाठ है।",
                "मैं आज बहुत खुश हूं क्योंकि मौसम बहुत अच्छा है।",
                "हमारी भारतीय संस्कृति बहुत समृद्ध है।"
            ]
            tokenizer.train_from_iterator(basic_texts, trainer)
            return tokenizer
            
    except Exception as e:
        st.error(f"Error initializing tokenizer: {str(e)}")
        st.info("Falling back to basic tokenizer...")
        # Create a basic tokenizer as fallback
        tokenizer = Tokenizer(models.BPE(unk_token="<unk>"))
        tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
        tokenizer.decoder = decoders.ByteLevel()
        return tokenizer

# Load the tokenizer
tokenizer = load_tokenizer()

# After loading the tokenizer, add this to display vocabulary info
vocab = tokenizer.get_vocab()
vocab_size = len(vocab)

# Add this after the title section
st.markdown(f"""
### Tokenizer Information:
- Total Vocabulary Size: {vocab_size} tokens
""")

# Optional: Add detailed token statistics
sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])
with st.expander("View Vocabulary Details"):
    st.markdown("#### Special Tokens:")
    special_tokens = ["<unk>", "<pad>", "<bos>", "<eos>"]
    for token in special_tokens:
        if token in vocab:
            st.write(f"- {token}: ID {vocab[token]}")
    
    st.markdown("#### Sample Tokens (first 20):")
    for token, id in sorted_vocab[:20]:
        if token not in special_tokens:
            st.write(f"- Token: {token}, ID: {id}")

def tokenize_text(text):
    """Tokenize input text and return tokens with statistics"""
    if tokenizer is None:
        return None
        
    try:
        encoding = tokenizer.encode(text)
        tokens = encoding.tokens
        
        # Calculate statistics
        original_length = len(text)
        tokenized_length = len(tokens)
        compression_ratio = original_length / tokenized_length if tokenized_length > 0 else 0
        
        return {
            "tokens": tokens,
            "original_length": original_length,
            "tokenized_length": tokenized_length,
            "compression_ratio": compression_ratio
        }
    except Exception as e:
        st.error(f"Error processing text: {str(e)}")
        return None

# Title and description
st.title("Hindi BPE Tokenizer")
st.markdown("""
This tokenizer implements Byte Pair Encoding for Hindi text with a vocabulary size < 5000 tokens.

### Features:
- Vocabulary size: < 5000 tokens
- Compression ratio: > 3.2
- Supports Hindi text
""")

# Example texts
example_texts = [
    "नमस्ते भारत! यह एक उदाहरण पाठ है।",
    "मैं आज बहुत खुश हूं क्योंकि मौसम बहुत अच्छा है।",
    "हमारी भारतीय संस्कृति बहुत समृद्ध है।"
]

# Initialize session state for selected example
if 'selected_example' not in st.session_state:
    st.session_state.selected_example = None

# Create two columns
col1, col2 = st.columns([2, 1])

with col2:
    # Example selector
    st.subheader("Try an example")
    for i, example in enumerate(example_texts):
        if st.button(f"Example {i+1}", key=f"example_{i}"):
            st.session_state.selected_example = example

with col1:
    # Text input
    default_text = st.session_state.selected_example if st.session_state.selected_example else ""
    text_input = st.text_area(
        "Enter Hindi text here",
        value=default_text,
        height=150,
        key="input_text"
    )

# Process text when input is available
if text_input:
    result = tokenize_text(text_input)
    
    if result:
        # Display results in an organized way
        st.markdown("### Results")
        
        # Display tokens
        st.markdown("#### Tokens")
        st.markdown('<div class="output-container">', unsafe_allow_html=True)
        st.write(result["tokens"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display statistics
        st.markdown("#### Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Original Length", result["original_length"])
        
        with col2:
            st.metric("Number of Tokens", result["tokenized_length"])
        
        with col3:
            st.metric("Compression Ratio", f"{result['compression_ratio']:.2f}")

# Footer
st.markdown("---")
st.markdown("""
### About
This tokenizer uses the `tokenizers` library to implement BPE encoding specifically for Hindi text.
For more information, visit our [GitHub Repository](https://github.com/dhruv369/ERA3/tree/main/S11).
""") 