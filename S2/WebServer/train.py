import torch
import torch.nn as nn
import torch.optim as optim
from model import DigitRecognitionModel, get_data_loaders
from utils import save_model

def train_model(epochs=5, batch_size=64, learning_rate=0.001, data_dir='./data'):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Use the get_data_loaders function from model.py
    train_loader, _ = get_data_loaders(batch_size, data_dir)
    
    model = DigitRecognitionModel().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            if i % 100 == 99:
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 100:.3f}')
                running_loss = 0.0

    print('Finished Training')
    save_model(model, 'digit_recognition_model.pth')
