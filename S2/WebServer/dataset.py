import torch
from torchvision import datasets, transforms

class MNISTDataset:
    def __init__(self, data_dir='./data'):
        self.data_dir = data_dir
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])

    def get_train_loader(self, batch_size, drop_last=False):
        train_dataset = datasets.MNIST(self.data_dir, train=True, download=True, transform=self.transform)
        return torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True, drop_last=drop_last)

    def get_test_loader(self, batch_size, drop_last=False):
        test_dataset = datasets.MNIST(self.data_dir, train=False, download=True, transform=self.transform)
        return torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False, drop_last=drop_last)
