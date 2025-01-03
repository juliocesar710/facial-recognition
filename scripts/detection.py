import cv2
import numpy as np
from tensorflow.keras.models import load_model
from google.colab.patches import cv2_imshow

# Carregar o modelo treinado
model = load_model('model.h5')

# Função para pré-processar a face
def preprocess_face(face):
    face = cv2.resize(face, (128, 128))
    face = face / 255.0
    return np.expand_dims(face, axis=0)

# Função para classificar a face
def classify_face(image_path):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        prediction = model.predict(preprocess_face(face))
        label = 'Male' if prediction[0] > 0.5 else 'Female'
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2_imshow(image)

# Exemplo de uso
classify_face('path/to/image.jpg')
