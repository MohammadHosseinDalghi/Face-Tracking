# Importing Libraries
import cv2
import pyautogui as robot

# reading the haarcascade files
eye_model = cv2.CascadeClassifier("haarcascade_eye.xml")
face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")