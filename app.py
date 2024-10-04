from flask import Flask, request, render_template
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import time

app = Flask(__name__)

# Load the trained model (assuming it's in the same folder as this file)
model = load_model('pneumonia_model.h5')

# Define the folder where uploaded images will be saved
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'img')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist


@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML page


@app.route('/predict', methods=['POST'])
def predicts():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']

        # Ensure file is uploaded
        if not file:
            return render_template('index.html', prediction='No file uploaded')

        # Save the uploaded image with a unique filename
        unique_filename = f"uploaded_image_{int(time.time())}.jpg"
        img_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(img_path)  # Save the uploaded image

        # Process the uploaded image for prediction
        img = image.load_img(img_path, target_size=(150, 150))  # Resize image
        img_array = image.img_to_array(img)  # Convert to array
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Make prediction
        prediction = model.predict(img_array)
        result = 'Pneumonia' if prediction[0][0] > 0.5 else 'Normal'

        return render_template('index.html', prediction=result)  # Display the result


if __name__ == '__main__':
    app.run(debug=True)
