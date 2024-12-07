from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Store the current image in memory
current_image = None

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global current_image
    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    current_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert to base64 for display
    _, buffer = cv2.imencode('.jpg', current_image)
    img_str = base64.b64encode(buffer).decode()
    
    return JSONResponse({
        "message": "File uploaded successfully",
        "image": f"data:image/jpeg;base64,{img_str}"
    })

@app.post("/preprocess/{method}")
async def preprocess_image(method: str):
    global current_image
    
    if current_image is None:
        return JSONResponse({"error": "No image loaded"})
    
    processed_image = current_image.copy()
    
    if method == "grayscale":
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)
    elif method == "blur":
        processed_image = cv2.GaussianBlur(processed_image, (5, 5), 0)
    elif method == "edge":
        gray = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.Canny(gray, 100, 200)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGR)
    
    current_image = processed_image
    
    # Convert to base64 for display
    _, buffer = cv2.imencode('.jpg', current_image)
    img_str = base64.b64encode(buffer).decode()
    
    return JSONResponse({
        "image": f"data:image/jpeg;base64,{img_str}"
    })

@app.post("/augment/{method}")
async def augment_image(method: str):
    global current_image
    
    if current_image is None:
        return JSONResponse({"error": "No image loaded"})
    
    augmented_image = current_image.copy()
    
    if method == "rotate":
        augmented_image = cv2.rotate(augmented_image, cv2.ROTATE_90_CLOCKWISE)
    elif method == "flip":
        augmented_image = cv2.flip(augmented_image, 1)
    elif method == "brightness":
        augmented_image = cv2.convertScaleAbs(augmented_image, alpha=1.2, beta=30)
    
    current_image = augmented_image
    
    # Convert to base64 for display
    _, buffer = cv2.imencode('.jpg', current_image)
    img_str = base64.b64encode(buffer).decode()
    
    return JSONResponse({
        "image": f"data:image/jpeg;base64,{img_str}"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 