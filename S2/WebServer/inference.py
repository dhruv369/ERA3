import torch
from model import DigitRecognitionModel
from utils import load_model

def predict_digit(image_tensor):
    model = DigitRecognitionModel()
    model = load_model(model, 'digit_recognition_model.pth')
    model.eval()

    with torch.no_grad():
        if image_tensor.dim() == 3:
            image_tensor = image_tensor.unsqueeze(0)
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        return predicted.item()
