# Session 5 : Readme File

# MNIST Model with Constraints

This repository contains an implementation of a lightweight MNIST-based neural network model designed to meet specific requirements. The model and associated code ensure efficient training and robust performance.

## Objectives

1. **Model Characteristics**:
   - Less than **25,000 parameters**.
   - Achieves **95%+ training accuracy in 1 epoch**.

2. **GitHub Actions Testing**:
   - Verify the model has less than 25,000 parameters.
   - Confirm training accuracy of 95% or more in 1 epoch.

3. **Advanced Features**:
   - Add image augmentation and demonstrate augmented samples.
   - Include additional tests with GitHub Actions.

---

## Features

### Base Tasks
- **Model Implementation**:
  - A lightweight neural network with fewer than 25,000 parameters.
  - Achieves 95%+ accuracy on the MNIST dataset within 1 epoch.

- **GitHub Actions**:
  - Automated tests to validate model characteristics.
  - Includes:
    - Parameter count check.
    - Accuracy validation in one epoch.

- **Artifacts**:
  - Screenshots of successful tests.
  - Links to GitHub Actions and README.md.

### Advanced Tasks
- **Image Augmentation**:
  - Applied augmentation techniques (rotation, flipping, scaling, etc.).
  - Screenshots showcasing augmented images.

- **Additional Tests**:
  - Three custom tests for advanced validation.

- **Build Badge**:
  - "Build Pass" badge added to this README file.

---

## Setup and Usage

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Libraries: TensorFlow, NumPy, Matplotlib, GitHub CLI

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dhruv369/ERA3.git
   cd ERA3/S4
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the training script:
   ```bash
   python train.py
   ```

### Testing with GitHub Actions
1. Push your changes to GitHub.
2. GitHub Actions will automatically:
   - Check parameter count.
   - Validate training accuracy.
3. View results under the **Actions** tab on your GitHub repository.

---

## Results

### Base
- **GitHub Actions Tests**:
  - ![Screenshot of Successful Tests](./screenshots/successful_tests.png)
- **Links**:
  - [GitHub Actions Results](https://github.com/dhruv369/ERA3/actions)
  - [README.md](https://github.com/dhruv369/ERA3/blob/main/S4/README.md)

### Advanced
- **Augmented Samples**:
  - ![Augmented Image Samples](./screenshots/augmented_samples.png)
- **Additional Tests**:
  - Python code included in `tests/` directory.

- **Build Badge**:
  - ![Build Pass](https://img.shields.io/github/actions/workflow/status/dhruv369/ERA3/build.yml)

---

## File Structure
- `train.py` - Script for training the MNIST model.
- `test_model.py` - Automated tests for GitHub Actions.
- `requirements.txt` - Dependencies for the project.
- `README.md` - Project documentation.
- `screenshots/` - Folder for test and result screenshots.

---

## Contributing
Feel free to fork this repository and submit a pull request. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
