import pytest
import torch
import torch.nn as nn
import os
import sys
import time

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import MNISTNet
from model.train import train_model

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def test_parameter_count():
    model = MNISTNet()
    param_count = count_parameters(model)
    assert param_count < 25000, f"Model has {param_count} parameters, should be less than 25000"

def test_training_accuracy():
    model, accuracy = train_model()
    assert accuracy >= 95.0, f"Model achieved {accuracy}% accuracy, should be >= 95%"

def test_model_overfitting():
    """Test if model can overfit on a small batch"""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = MNISTNet().to(device)
    x = torch.randn(10, 1, 28, 28).to(device)
    y = torch.randint(0, 10, (10,)).to(device)
    
    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.NLLLoss()
    
    for _ in range(100):
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
    
    pred = output.argmax(dim=1)
    accuracy = (pred == y).float().mean().item()
    assert accuracy > 0.5, "Model failed to overfit on small batch"

def test_model_save_load():
    """Test model saving and loading"""
    model = MNISTNet()
    torch.save(model.state_dict(), 'test_model.pth')
    
    loaded_model = MNISTNet()
    loaded_model.load_state_dict(torch.load('test_model.pth'))
    
    # Clean up
    os.remove('test_model.pth')
    assert True, "Model save/load test passed"

def test_inference_speed():
    """Test model inference speed"""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = MNISTNet().to(device)
    model.eval()
    x = torch.randn(1, 1, 28, 28).to(device)
    
    # Warmup
    with torch.no_grad():
        _ = model(x)
    
    # Measure time
    start_time = time.time()
    with torch.no_grad():
        _ = model(x)
    end_time = time.time()
    
    inference_time = (end_time - start_time) * 1000  # Convert to ms
    assert inference_time < 100, f"Inference too slow: {inference_time:.2f}ms"