# Importing Libraries
import cv2
import pyautogui as robot

# reading the haarcascade files
eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")
face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 
loop = True
cam = cv2.VideoCapture(0)

def face_detect(loop, camera, face_model, eye_model):
    _, img = camera.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_model.detectMultiScale(gray)