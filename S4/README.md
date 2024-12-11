# Session 4 : Readme File

# MNIST Model Training and Comparison

This repository provides a comprehensive implementation of a neural network for the MNIST dataset with additional features to compare model architectures and analyze their performance. The project is structured in two parts:

1. **Base Assignment**: Train a model and display training logs in a user-friendly frontend.
2. **Advanced Assignment**: Compare two models with different architectures using a custom frontend interface.

## Base Assignment
### Features
- Train a neural network on the MNIST dataset.
- Display live training logs in a frontend interface.
- Save a short video showcasing training logs and the frontend updates.

### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/dhruv369/ERA3.git
   cd S4
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model and view logs:
   ```bash
   python base_assignment/train_and_log.py
   ```
4. Generate a video of the logs and frontend:
   - Use your preferred screen recording software.

## Advanced Assignment
### Features
- Compare two models with different architecture configurations (e.g., kernel sizes, number of filters).
- Overlap results (loss and accuracy) on a single graph for easy comparison.
- Interactive frontend to:
  - Specify model configurations (e.g., `16, 32, 64` vs. `8, 8, 8`).
  - Train models sequentially and display comparison results.

### Additional Features
You can add the following for extra credit:
- Change optimizer (e.g., Adam, SGD).
- Modify batch size.
- Adjust the number of epochs.

### Usage
1. Start the frontend for model comparison:
   ```bash
   python advanced_assignment/model_comparison_interface.py
   ```
2. Specify configurations for the two models.
3. Train both models and view the results in real-time.
4. Save a video showing the comparison results and frontend functionality.

## Repository Structure
```
.
├── base_assignment        # Scripts and modules for base assignment
├── advanced_assignment    # Scripts and modules for advanced assignment
├── data                   # Scripts for data loading and preprocessing
├── tests                  # Test scripts for GitHub Actions
├── results                # Results, screenshots, and logs
├── frontend               # Frontend interface scripts
├── .github/workflows      # GitHub Actions configuration files
├── README.md              # Project documentation
└── requirements.txt       # Required dependencies
```

## GitHub Actions Workflow
The following tests are executed automatically via GitHub Actions:

### Base Tests
- **Training logs display**: Verifies that training logs are correctly displayed in the frontend.

### Advanced Tests
- **Model comparison**: Ensures the interface correctly compares two models.
- **Custom Tests**:
  1. **Optimizer switching**: Verifies training results using different optimizers.
  2. **Batch size adjustment**: Confirms training behavior for different batch sizes.
  3. **Epoch modification**: Checks training results for varying epochs.

## Results
- **Training logs video**: [View here](results/training_logs_video.mp4)
- **Model comparison video**: [View here](results/model_comparison_video.mp4)
- **Link to GitHub Actions**: [GitHub Actions](https://github.com/dhruv369/ERA3/actions)

## Advanced Features
- **Frontend Interface**: User-friendly interface for model training and comparison.
- **Build Pass Badge**: ![Build Status](https://github.com/dhruv369/ERA3/actions/workflows/main.yml/badge.svg)

## Contribution
Contributions are welcome! Please open an issue or submit a pull request for review.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
[Your Name](https://github.com/dhruv369)
