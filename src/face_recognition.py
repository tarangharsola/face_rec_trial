import os
import cv2
import numpy as np
import joblib

class FaceRecognizer:
    def __init__(self, model_path):
        # Check if the model file exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        # Load the pre-trained model
        self.model = joblib.load(model_path)

    def detect_faces(self, frame):
        """
        Detect faces in a given frame using Haar cascades.
        """
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Load the Haar cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if face_cascade.empty():
            raise RuntimeError("Haar cascade file not found or OpenCV is not installed correctly.")
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        return faces

    def recognize_faces(self, frame, faces):
        """
        Recognize faces in the given frame using the pre-trained model.
        """
        if not faces:
            # Return an empty list if no faces are detected
            return []
        
        recognized_faces = []
        for (x, y, w, h) in faces:
            # Extract the face region
            face = frame[y:y+h, x:x+w]
            
            # Resize the face to match the model's input size
            face = cv2.resize(face, (128, 128))
            
            # Flatten and normalize the face image
            face = face.flatten() / 255.0
            
            # Predict the label using the model
            label = self.model.predict([face])
            
            # Append the label and face coordinates to the results
            recognized_faces.append((label[0], (x, y, w, h)))
        
        return recognized_faces