from ultralytics import YOLO
import cv2
import time

# Load YOLO model for plate detection
model = YOLO("best_scabies.pt")
result = model.predict(source=0, show=True)