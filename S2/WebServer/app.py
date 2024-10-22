from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import predict_digit
import base64
import numpy as np
from PIL import Image
import io
import torch
import torchvision.transforms as transforms
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/identify', methods=['POST'])
def identify():
    data = request.json
    image_data = data['image'].split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    image = image.convert('L').resize((28, 28))
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    image_tensor = transform(image).unsqueeze(0)
    
    predicted_digit = predict_digit(image_tensor)
    return jsonify({'digit': str(predicted_digit)})

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
