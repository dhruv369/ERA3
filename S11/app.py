import streamlit as st
from tokenizers import Tokenizer, models, pre_tokenizers, decoders
import json
import os

# Page configuration
st.set_page_config(
    page_title="Hindi BPE Tokenizer",
    page_icon="🇮🇳",
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
            st.warning("Tokenizer file not found. Please run train_tokenizer.py first.")
            # Create a basic tokenizer as fallback
            tokenizer = Tokenizer(models.BPE())
            tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
            tokenizer.decoder = decoders.ByteLevel()
            return tokenizer
    except Exception as e:
        st.error(f"Error initializing tokenizer: {str(e)}")
        return None

# Load the tokenizer
tokenizer = load_tokenizer()

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

if tokenizer is None:
    st.error("Tokenizer is not properly initialized. Please make sure to run train_tokenizer.py first.")
    st.stop()

# Example texts
example_texts = [
    "नमस्ते भारत! यह एक उदाहरण पाठ है।",
    "मैं आज बहुत खुश हूं क्योंकि मौसम बहुत अच्छा है।",
    "हमारी भारतीय संस्कृति बहुत समृद्ध है।"
]

# Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Text input
    text_input = st.text_area(
        "Enter Hindi text here",
        height=150,
        key="input_text"
    )

with col2:
    # Example selector
    st.subheader("Try an example")
    for i, example in enumerate(example_texts):
        if st.button(f"Example {i+1}", key=f"example_{i}"):
            text_input = example
            st.session_state.input_text = example

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