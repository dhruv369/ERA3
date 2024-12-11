import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
import json
import os
from datetime import datetime

class MNISTTrainer:
    def __init__(self):
        self.model = None
        self.history = None
        self.logs_path = os.path.join('results', 'training_logs.json')
        
        # Create results directory if it doesn't exist
        os.makedirs('results', exist_ok=True)

    def load_data(self):
        (self.x_train, self.y_train), (self.x_test, self.y_test) = tf.keras.datasets.mnist.load_data()
        # Normalize pixel values
        self.x_train = self.x_train.astype('float32') / 255
        self.x_test = self.x_test.astype('float32') / 255
        
        # Reshape for CNN
        self.x_train = self.x_train.reshape(-1, 28, 28, 1)
        self.x_test = self.x_test.reshape(-1, 28, 28, 1)

    def create_model(self):
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

    def custom_callback(self):
        class LogCallback(tf.keras.callbacks.Callback):
            def __init__(self, logs_path):
                super().__init__()
                self.logs_path = logs_path
                self.logs = []

            def on_epoch_end(self, epoch, logs=None):
                log_entry = {
                    'epoch': epoch + 1,
                    'loss': float(logs['loss']),
                    'accuracy': float(logs['accuracy']),
                    'val_loss': float(logs['val_loss']),
                    'val_accuracy': float(logs['val_accuracy']),
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.logs.append(log_entry)
                
                # Save logs after each epoch
                with open(self.logs_path, 'w') as f:
                    json.dump(self.logs, f, indent=2)

        return LogCallback(self.logs_path)

    def train(self, epochs=10, batch_size=32):
        callback = self.custom_callback()
        
        self.history = self.model.fit(
            self.x_train, self.y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=0.2,
            callbacks=[callback]
        )

if __name__ == '__main__':
    trainer = MNISTTrainer()
    trainer.load_data()
    trainer.create_model()
    trainer.train() 