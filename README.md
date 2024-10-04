# pneumonia_ML
Pneumonia Detection Web Application
This project is a web-based application that uses a Convolutional Neural Network (CNN) to detect pneumonia from chest X-ray images. It is built using Flask for the backend, with a responsive frontend powered by Bootstrap. The model predicts whether a given chest X-ray shows signs of pneumonia or is normal.

Features
Image Upload: Users can upload chest X-ray images directly through the web interface.
Model Prediction: The app uses a trained CNN model (implemented using TensorFlow and Keras) to classify the image as either 'Pneumonia' or 'Normal'.
Interactive Interface: The web interface is clean, user-friendly, and responsive, offering immediate feedback after image submission.
Flask Backend: The app is powered by a Flask backend that handles model inference and image processing.
Bootstrap Frontend: The frontend is styled using Bootstrap for a modern, professional look that is mobile-responsive.
Technologies Used
Flask: Lightweight web framework for building the application backend.
TensorFlow & Keras: Used for building and loading the pre-trained pneumonia detection model.
OpenCV: For image preprocessing and manipulation.
Bootstrap: For styling and making the frontend responsive.
Jinja2: For rendering dynamic templates within Flask.
Folder Structure
graphql
Copy code
pneumonia_ML/
│
├── app.py                   # Main Flask app
├── pneumonia_model.h5        # Pre-trained CNN model for pneumonia detection
├── templates/
│   └── index.html            # Frontend HTML file (Bootstrap integrated)
└── saved IMG/                # Directory where uploaded images are saved
How to Run the Project Locally
Clone the repository:

bash
Copy code
git clone https://github.com/barrack81/pneumonia_ML.git
cd pneumonia-detection-app
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows use 'venv\Scripts\activate'
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
flask run
Access the app in your browser:

Open http://127.0.0.1:5000/ in your browser to upload an image and receive the pneumonia prediction.
Model Details
The model used in this project is a Convolutional Neural Network (CNN) trained on a dataset of chest X-ray images. The dataset contains labeled images of both normal lungs and lungs affected by pneumonia, and the model was trained to distinguish between the two. The model was saved as an .h5 file and is loaded into the Flask app to make real-time predictions.

Future Enhancements
Model Optimization: Improving the accuracy of the model by experimenting with more complex architectures or fine-tuning the existing model.
Dataset Expansion: Incorporating a larger, more diverse dataset to improve the robustness of the model.
Additional Features: Adding functionality for multi-disease detection or allowing for more complex image analysis.
License
This project is licensed under the MIT License - see the LICENSE file for details