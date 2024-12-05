# Session 2 : Readme File

# Assignment: Multi-Modal Preprocessing & Augmentation App

This repository contains an application built using **FastAPI** to demonstrate the processing pipeline for various data types: **Text**, **Image**, **Audio**, and **3D files**. The application provides functionalities to:

1. **Load a data file** and display one sample.
2. **Preprocess the data** and show the transformed output.
3. **Augment the data** and display the augmented version.

## Table of Contents

- [Features](#features)
- [Data Types Supported](#data-types-supported)
- [How to Run the Application](#how-to-run-the-application)
- [Dependencies](#dependencies)
---

## Features

- **Data Upload**: Upload a file for processing (text, image, audio, or 3D).
- **Preprocessing**: Modify the data (e.g., cleaning text, resizing images, filtering audio, or normalizing 3D models).
- **Augmentation**: Apply transformations like augmenting text data, applying image filters, modifying audio pitch, or perturbing 3D geometries.

---

## Data Types Supported

1. **Text** (Mandatory)
   - Preprocessing: Text cleaning, removing stop words.
   - Augmentation: Synonym replacement, paraphrasing.
2. **Image**
   - Preprocessing: Resize, crop, normalize.
   - Augmentation: Flip, rotate, change brightness.
3. **Audio**
   - Preprocessing: Noise removal, normalization.
   - Augmentation: Pitch shifting, time-stretching.
4. **3D Files (.off format)**
   - Preprocessing: Normalization, vertex cleaning.
   - Augmentation: Scale, rotate, add noise.

---

## How to Run the Application

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dhruv369/ERA3
   cd S3
---

### **When to Keep Additional Info Separate**


1. **`requirements.txt`**:
   - List all Python dependencies with version numbers.
   - Example:
     ```
     fastapi==0.95.0
     numpy>=1.21
     pandas
     pillow
     ```

2. **`install requirements`**:
   - pip install -r requirements.txt

---

