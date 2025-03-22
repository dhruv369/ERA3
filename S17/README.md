---
title: Stable Diffusion
emoji: 🖼
colorFrom: purple
colorTo: red
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
---

# Stable Diffusion Textual Inversion Styles

This project explores Stable Diffusion textual inversion concepts with custom style applications and loss functions.

## Project Structure
```
.
├── app.py              # Gradio web application
├── models/            # Directory for storing learned_embeds.bin files
├── utils/             # Utility functions including custom loss
├── outputs/           # Generated images directory
└── requirements.txt   # Project dependencies
```

## Features
- Integration with 5 different textual inversion styles
- Custom loss function implementation
- Interactive web interface using Gradio
- Image generation with style mixing

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download the textual inversion embeddings to the `models` directory
3. Run the web app:
```bash
python app.py
```

## Styles Used
1. [Style 1 - Analog Film]
2. [Style 2 - Watercolor]
3. [Style 3 - Cyberpunk Anime]
4. [Style 4 - Arcane Style]
5. [Style 5 - Midjourney Style]

## Custom Loss Function
Implementation of a custom loss function for image processing.

## Links
- [Hugging Face Space](https://huggingface.co/spaces/Dhruv3690/Stable_Diffusion)

