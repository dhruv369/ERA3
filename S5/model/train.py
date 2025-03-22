import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from model import MNISTNet
from tqdm import tqdm

def train_model():
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Enhanced data transformations with augmentation
    transform = transforms.Compose([
        transforms.RandomRotation(5),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    # Load MNIST dataset
    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=512, shuffle=True)
    
    # Initialize model, optimizer and criterion
    model = MNISTNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.003)
    criterion = nn.NLLLoss()
    
    # Training loop
    model.train()
    correct = 0
    processed = 0
    
    pbar = tqdm(train_loader)
    for batch_idx, (data, target) in enumerate(pbar):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        
        output = model(data)
        loss = criterion(output, target)
        
        loss.backward()
        optimizer.step()
        
        pred = output.argmax(dim=1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)
        
        pbar.set_description(f'Loss={loss.item():0.4f} Accuracy={100*correct/processed:0.2f}%')
    
    return model, 100*correct/processed

if __name__ == "__main__":
    model, accuracy = train_model()
    print(f"Final Training Accuracy: {accuracy}%")
    
    # Save model
    torch.save(model.state_dict(), 'results/mnist_model.pth') 