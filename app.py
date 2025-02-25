import os
import cv2
import numpy as np
import tensorflow as tf
import base64
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from pydicom import dcmread
from io import BytesIO
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load pre-trained autoencoder model
MODEL_PATH = "models/autoencoder_noise.h5"

if os.path.exists(MODEL_PATH):
    autoencoder = load_model(MODEL_PATH)
else:
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found. Please check the path.")

# Function to load and preprocess image
def load_image(file):
    ext = os.path.splitext(file.filename)[-1].lower()
    if ext == ".dcm":
        dicom = dcmread(file)
        img = dicom.pixel_array.astype(np.float32)
    else:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE).astype(np.float32)

    img = cv2.resize(img, (200, 200))  # Resize image for model
    img = np.repeat(img[..., np.newaxis], 3, -1)  # Convert grayscale to 3-channel
    img = img / 255.0  # Normalize to [0,1]
    return img

# Function to denoise image
def denoise_image(model, image):
    image_expanded = np.expand_dims(image, axis=0)  # Add batch dimension
    denoised_image = model.predict(image_expanded)
    return np.squeeze(denoised_image)  # Remove batch dimension

# Function to convert image to Base64
def image_to_base64(image):
    _, buffer = cv2.imencode('.png', (image * 255).astype(np.uint8))
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    original_image = load_image(file)
    original_base64 = image_to_base64(original_image)
    return jsonify({"original_image": original_base64})

@app.route("/denoise", methods=["POST"])
def denoise():
    if "image" not in request.json:
        return jsonify({"error": "No image data provided"}), 400
    
    # Extract base64 image and convert back to numpy array
    image_data = request.json["image"].split(",")[1]
    img_bytes = base64.b64decode(image_data)
    img_array = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
    img = cv2.resize(img, (200, 200))
    img = np.repeat(img[..., np.newaxis], 3, -1)

    # Denoise the image
    denoised_image = denoise_image(autoencoder, img)
    denoised_base64 = image_to_base64(denoised_image)
    
    return jsonify({"denoised_image": denoised_base64})

if __name__ == "__main__":
    app.run(debug=True)