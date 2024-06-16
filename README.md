# Potato Disease Detection using Deep Learning

This project demonstrates the power of deep learning to accurately identify common potato leaf diseases, specifically Early Blight and Late Blight, compared to healthy leaves. This early detection system can empower farmers and agricultural experts to take timely action, potentially saving crops and improving yields.

## Key Features:

- **Image Classification:** Leverages a Convolutional Neural Network (CNN) trained on a dataset of potato leaf images exhibiting signs of disease or good health.
- **User-Friendly Web App:** Built using Streamlit, the application provides a simple interface for users to upload leaf images and receive instant disease predictions.
- **Data Augmentation:** Employs techniques like random flipping and rotation to increase the training dataset size, enhancing the model's ability to generalize to new images.
- **Performance Visualization:** The training process is visualized with graphs, tracking accuracy and loss over time, offering insights into model learning.

## Potential Impact:

- **Early Disease Identification:** Helps farmers intervene quickly, preventing widespread disease outbreaks.
- **Reduced Crop Loss:** Timely treatment based on accurate predictions can significantly reduce yield losses.
- **Optimized Resource Use:** Prevents unnecessary pesticide application by targeting only affected areas.

## Technologies Used:

- Python
- TensorFlow
- Keras
- Streamlit
- Matplotlib

## How to Use:

1. Clone the repository.
   ```bash
   git clone https://github.com/Mani242002/POTATO-LEAF-DISEASE-CLASSIFICATION
2. Install the required dependencies.
   ```bash
    pip install -r requirements.txt
3. Run the Streamlit application.
   ```bash
   streamlit run app.py
4. Upload an image of a potato leaf.
5. Receive the predicted disease classification and confidence score.


   
