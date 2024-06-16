import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the model
model = tf.keras.models.load_model('potato_disease_classification.keras')


# Define the class names
class_names = ['Potato___Early_blight', 'Potato___Late_blight','Potato___healthy' ]

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to match the input shape of the model
    image = image.resize((256, 256))
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Expand the dimensions to create a batch of size 1
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Function to make predictions
def predict_disease(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Make prediction
    prediction = model.predict(processed_image)
    # Get the predicted class
    print(prediction)
    predicted_class = class_names[np.argmax(prediction[0])]
    # Get the confidence score
    confidence = np.max(prediction) * 100
    return predicted_class, confidence

# Streamlit UI
st.title("Potato Leaf Disease Classification")
st.write("Upload an image of a potato leaf to classify its disease.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction on the uploaded image
    predicted_class, confidence = predict_disease(image)

    # Display the prediction
    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")
