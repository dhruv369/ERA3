from .model import MNISTNet
from torchsummary import torchsummary

def print_model_summary():
    model = MNISTNet()
    torchsummary.summary(model, (1, 28, 28))

if __name__ == "__main__":
    print_model_summary() 