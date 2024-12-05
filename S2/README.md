# Session 2 : Readme File

# MNIST Digit Recognition

This project implements a Convolutional Neural Network (CNN) for recognizing handwritten digits using the MNIST dataset. It includes a model definition, training script, and a web interface for making predictions.

## Project Structure

- `model.py`: Defines the CNN architecture and training functions.
- `dataset.py`: Handles data loading and preprocessing for the MNIST dataset.
- `app.py`: Flask web application for serving predictions.
- `main.py`: Entry point for training the model.
- `inference.py`: Functions for making predictions on new data.
- `index.html`: HTML template for the web interface.
- `utils.py`: Utility functions used across the project.
- `train.py`: Script for training the model.

## Requirements

- Python 3.7+
- PyTorch
- torchvision
- Flask
- NumPy

## Installation

1. Clone this repository:   ```
   git clone https://github.com/your-username/mnist-digit-recognition.git
   cd mnist-digit-recognition   ```

2. Install the required packages:   ```
   pip install -r requirements.txt   ```

## Usage

### Training the Model

To train the model, run:
