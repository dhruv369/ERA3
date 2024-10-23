import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import numpy as np
import torch.nn.functional as F
from dataset import MNISTDataset

class DigitRecognitionModel(nn.Module):
    def __init__(self):
        super(DigitRecognitionModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 64, 3)
        self.pool = nn.MaxPool2d(2, 2)
        # Calculate the correct input size for fc1
        self.fc1 = nn.Linear(64 * 3 * 3, 64)  # Changed from 64 * 4 * 4
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = F.relu(self.conv3(x))
        # Add a print statement to check the shape
        print(f"Shape before flattening: {x.shape}")
        x = x.view(x.size(0), -1)  # Flatten the tensor
        # Add another print statement after flattening
        print(f"Shape after flattening: {x.shape}")
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def create_model():
    return DigitRecognitionModel()

def get_data_loaders(batch_size=64, data_dir='./data'):
    dataset = MNISTDataset(data_dir=data_dir)
    train_loader = dataset.get_train_loader(batch_size, drop_last=True)
    test_loader = dataset.get_test_loader(batch_size, drop_last=True)  # Changed to True
    
    print(f"Train dataset size: {len(train_loader.dataset)}")
    print(f"Test dataset size: {len(test_loader.dataset)}")
    print(f"Number of training batches: {len(train_loader)}")
    print(f"Number of test batches: {len(test_loader)}")
    
    return train_loader, test_loader

def train_model(model, train_loader, test_loader, num_epochs=3, learning_rate=0.001):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            
            # Add a print statement to check input shape
            print(f"Input shape: {data.shape}")
            
            output = model(data)
            
            print(f"Epoch {epoch+1}, Batch {batch_idx}: Output shape: {output.shape}, Target shape: {target.shape}")
            
            # Handle potential batch size mismatch
            if output.shape[0] != target.shape[0]:
                print(f"Batch size mismatch detected. Adjusting output and target.")
                min_size = min(output.shape[0], target.shape[0])
                output = output[:min_size]
                target = target[:min_size]
            
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

        if total > 0:
            train_accuracy = 100 * correct / total
            avg_loss = total_loss / len(train_loader)
            print(f'Epoch {epoch+1}/{num_epochs}, Train Loss: {avg_loss:.4f}, Train Accuracy: {train_accuracy:.2f}%')
        else:
            print(f'Epoch {epoch+1}/{num_epochs}, No valid batches processed.')

        # Evaluation phase
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for data, target in test_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                _, predicted = torch.max(output.data, 1)
                total += target.size(0)
                correct += (predicted == target).sum().item()

        if total > 0:
            test_accuracy = 100 * correct / total
            print(f'Epoch {epoch+1}/{num_epochs}, Test Accuracy: {test_accuracy:.2f}%')
        else:
            print(f'Epoch {epoch+1}/{num_epochs}, No valid test batches processed.')

    torch.save(model.state_dict(), 'digit_recognition_model.pth')
    print('Training completed. Model saved.')

if __name__ == '__main__':
    model = create_model()
    train_loader, test_loader = get_data_loaders()
    train_model(model, train_loader, test_loader)
