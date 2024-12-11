import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

def show_augmented_samples():
    # Define the augmentation transforms
    transform = transforms.Compose([
        transforms.RandomRotation(5),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
    ])
    
    # Load MNIST dataset
    dataset = datasets.MNIST('./data', train=True, download=True)
    
    # Create a figure with subplots
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))
    
    # Get one image
    image, label = dataset[0]
    
    # Apply different augmentations
    for i in range(3):
        for j in range(3):
            # Apply transform
            augmented = transform(image)
            # Convert to numpy and plot
            axes[i,j].imshow(augmented.squeeze(), cmap='gray')
            axes[i,j].axis('off')
            axes[i,j].set_title(f'Augmented {i*3+j+1}')
    
    plt.tight_layout()
    plt.savefig('images/augmented_samples.png')
    plt.close()

if __name__ == "__main__":
    show_augmented_samples() 