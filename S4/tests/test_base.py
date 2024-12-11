import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base_assignment.train_and_log import MNISTTrainer

def test_model_creation():
    trainer = MNISTTrainer()
    trainer.create_model()
    assert trainer.model is not None

def test_data_loading():
    trainer = MNISTTrainer()
    trainer.load_data()
    assert trainer.x_train is not None
    assert trainer.y_train is not None
    assert trainer.x_test is not None
    assert trainer.y_test is not None 