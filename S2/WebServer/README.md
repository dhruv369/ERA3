# MNIST Digit Recognition and Animal Selector

This project implements a Convolutional Neural Network (CNN) for recognizing handwritten digits using the MNIST dataset. It also includes a web interface for selecting animals and uploading files.

## Project Structure

- `model.py`: Defines the CNN architecture and training functions.
- `dataset.py`: Handles data loading and preprocessing for the MNIST dataset.
- `app.py`: Flask web application for serving predictions and handling animal selection and file uploads.
- `main.py`: Entry point for training the model.
- `inference.py`: Functions for making predictions on new data.
- `templates/index.html`: HTML template for the web interface.
- `utils.py`: Utility functions used across the project.
- `train.py`: Script for training the model.
- `static/`: Contains CSS, JavaScript, and image files for the web interface.

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
