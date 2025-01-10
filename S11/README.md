---
title: BPE Tokenizer for Hindi Language
emoji: 🇮🇳
colorFrom: blue
colorTo: red
sdk: streamlit
sdk_version: 1.31.1
app_file: app.py
pinned: false
---

# BPE Tokenizer for Hindi Language

This space provides a Byte Pair Encoding (BPE) tokenizer specifically trained for Hindi text. The tokenizer is designed to achieve efficient text compression while maintaining a vocabulary size under 5000 tokens.

## Features

- Vocabulary size < 5000 tokens
- Compression ratio > 3.2
- Special token handling
- Support for Hindi Unicode characters

## How to Use

1. Enter Hindi text in the input textbox
2. Or select one of the example texts
3. Results will show:
   - Generated tokens
   - Original text length
   - Number of tokens
   - Compression ratio

## Technical Details

- Built using the `tokenizers` library
- Implements Byte Pair Encoding algorithm
- Includes special tokens: `<unk>`, `<pad>`, `<bos>`, `<eos>`
- Interactive Streamlit interface

## Source Code

The complete source code is available at: [GitHub Repository](https://github.com/dhruv369/ERA3/tree/main/S11)

## Repository Structure

```
S11/
├── train_tokenizer.py       # Script to train the tokenizer
├── app.py                   # Streamlit web interface
├── example_data.txt         # Sample text data for training
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore configuration
└── README.md               # Documentation
```

