# Session 5 : Readme File

# MNIST Model with Efficient Parameters

This repository contains an efficient implementation of a neural network for the MNIST dataset. The model is designed to meet the following requirements:

## Model Characteristics
- **Less than 25,000 parameters**
- **Achieves 95% or higher training accuracy in 1 epoch**

## Repository Structure
```
.
├── data                # Scripts for data loading and preprocessing
├── model               # Model definition and architecture
├── tests               # Test scripts for GitHub Actions
├── results             # Results, screenshots, and logs
├── images              # Augmented image samples (for Advanced section)
├── .github/workflows   # GitHub Actions configuration files
├── README.md           # Project documentation
└── requirements.txt    # Required dependencies
```

## How to Use

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/dhruv369/ERA3.git
   cd S5
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run Training
1. Train the model:
   ```bash
   python model/train.py
   ```
2. View augmented image samples (Advanced):
   ```bash
   python data/augment_samples.py
   ```

### Run Tests
1. Ensure GitHub Actions are properly set up by committing your code.
2. To run tests locally:
   ```bash
   pytest tests/
   ```

## GitHub Actions Workflow
The following tests are executed automatically via GitHub Actions:

### Base Tests
- **Parameter count**: Ensures the model has fewer than 25,000 parameters.
- **Training accuracy**: Confirms the model achieves 95% or higher accuracy within 1 epoch.

### Advanced Tests
- **Image augmentation**: Generates and validates augmented image samples.
- **Custom tests**:
  1. Overfitting test: Ensures the model can overfit on a small dataset.
  2. Inference speed test: Confirms inference time is within acceptable limits.
  3. Model saving/loading: Validates the model can be saved and loaded without accuracy loss.

## Results
- **Screenshot of GitHub Actions passing tests**: [View here](results/github_actions_screenshot.png)
- **Link to GitHub Actions**: [GitHub Actions](https://github.com/dhruv369/ERA3/actions)

## Advanced Features
- **Image Augmentation**: Samples of augmented images are available in the `images/` directory.
- **Build Pass Badge**: ![Build Status](https://github.com/dhruv369/ERA3/actions/workflows/main.yml/badge.svg)

## Contribution
Contributions are welcome! Please open an issue or submit a pull request for review.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
[Your Name](https://github.com/dhruv369)
