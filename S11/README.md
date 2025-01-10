# Session 11 Assignment: BPE Tokenizer for an Indian Language

This repository contains the implementation of a Byte Pair Encoding (BPE) tokenizer for an Indian language. The tokenizer is trained to satisfy the following requirements:

1. Vocabulary size is **less than 5000 tokens**.
2. Compression ratio is **3.2 or above**.

The tokenizer is implemented using the `tokenizers` library and is designed to handle text data efficiently for the chosen language.

---

## Repository Structure

```
S11/
├── train_bpe_tokenizer.ipynb  # Jupyter notebook to train the tokenizer
├── bpe_tokenizer.json         # Saved BPE tokenizer model
├── example_data.txt           # Sample text data used for training
├── README.md                  # Documentation for the assignment
```

---

## Requirements

Install the required Python libraries before running the notebook:

```bash
pip install tokenizers gradio
```

---

## Training the Tokenizer

The tokenizer is trained using a dataset from the chosen Indian language. The training process includes:

1. **Dataset Preparation:** Preprocessing text data to remove noise and format it consistently.
2. **Tokenizer Initialization:** Initializing a BPE tokenizer with a vocabulary size limit of 5000.
3. **Training:** Running the training algorithm on the corpus.

### Key Parameters
- **Vocabulary Size:** 5000 tokens (maximum).
- **Special Tokens:** `<unk>`, `<pad>`, `<bos>`, `<eos>`.

The training script is provided in the `train_bpe_tokenizer.ipynb` file.

---

## Tokenizer Evaluation

### Vocabulary Size
After training, the vocabulary size is validated to ensure it is less than 5000 tokens:

```python
vocab_size = len(tokenizer.get_vocab())
print(f"Vocabulary Size: {vocab_size}")
```

### Compression Ratio
The compression ratio is computed using the formula:

\[ \text{Compression Ratio} = \frac{\text{Original Character Count}}{\text{Tokenized Character Count}} \]

Example calculation:

```python
text = "your text data here"
original_length = len(text)
tokenized_length = len(tokenizer.encode(text).tokens)
compression_ratio = original_length / tokenized_length
print(f"Compression Ratio: {compression_ratio}")
```

Results:
- **Vocabulary Size:** Less than 5000 tokens.
- **Compression Ratio:** Greater than 3.2.

---

## Usage

### Running the Tokenizer
You can use the tokenizer to tokenize text data:

```python
from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("bpe_tokenizer.json")

def tokenize_text(text):
    return tokenizer.encode(text).tokens

text = "Sample text in the chosen Indian language"
tokens = tokenize_text(text)
print(tokens)
```

### Hosted on HuggingFace Spaces
The tokenizer is deployed on HuggingFace Spaces with a simple Gradio interface. To try it out:

1. Visit the [HuggingFace Space](https://huggingface.co/spaces/your-space-name).
2. Enter your text in the input field to view tokenized output.

---

## How to Reproduce

1. Clone this repository:

```bash
git clone https://github.com/dhruv369/ERA3.git
cd ERA3/S11
```

2. Open the `train_bpe_tokenizer.ipynb` notebook in Jupyter or any compatible editor.
3. Follow the steps in the notebook to train and evaluate the tokenizer.

---

## Results

- **Vocabulary Size:** 4998 tokens (example result).
- **Compression Ratio:** 3.5 (example result).

---

## Future Work

1. Improve preprocessing for noise reduction in the dataset.
2. Explore additional special tokens to improve encoding efficiency.
3. Test the tokenizer with other Indian languages.

---

## Contact

For any questions or issues, feel free to open an issue on the repository or
 reach out at [dhruv.vyas3690@gmail..com](mailto:dhruv.vyas3690@gmail.com).

---

