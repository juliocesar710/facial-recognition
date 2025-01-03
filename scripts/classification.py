import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Carregar o modelo treinado
model = load_model('model.h5')

# Função para pré-processar a imagem
def preprocess_image(image):
    image = cv2.resize(image, (128, 128))
    image = image / 255.0
    return np.expand_dims(image, axis=0)

# Função para classificar imagem
def classify_uploaded_image(image_path):
    image = cv2.imread(image_path)
    prediction = model.predict(preprocess_image(image))
    label = 'Male' if prediction[0] > 0.5 else 'Female'
    print(f"A imagem enviada foi classificada como: {label}")

# Exemplo de uso
classify_uploaded_image('path/to/uploaded_image.jpg')
