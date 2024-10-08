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
    # We used the `flip` to show us the image like a mirror.
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_model.detectMultiScale(gray)
    # We wrote this if so that if our face goes out of the frame, don't give us tuple error.
    if len(face) > 0:
        xf = face[0][0]
        yf = face[0][1]
        xf2 = xf + face[0][2]
        yf2 = yf + face[0][3]
        gray_face = gray[yf:yf2, xf:yf2]
        eyes = eye_model.detectMultiScale(gray_face, minSize=(30, 30), scaleFactor=1.1, minNeighbors=5)
        imgout = img.copy()

    out = cv2.rectangle(imgout, (xf, yf), (xf2, yf2), (0,250,0), 3)