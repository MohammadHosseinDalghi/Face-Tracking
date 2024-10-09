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
    while loop:
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

        white = (250,250,250)
        red = (0,0,250)
        color = white
        
        #the location of mouse x
        mouse_x = robot.position().x
        #the location of mouse y
        mouse_y = robot.position().y

        if xf < 400:
            color = red
            # ith this command, we say that if the speed of our head is high, move the mouse faster
            mouse_x -= abs(xf-400)
            robot.moveTo(mouse_x, mouse_y, 0)
        
        if xf2 > 900:
            color = red
            mouse_x += abs(xf2 - 900)
            robot.moveTo(mouse_x, mouse_y, 0)

        if yf < 100:
            color = red
            mouse_y -= abs(yf - 100)
            robot.moveTo(mouse_x, mouse_y, 0)

        if yf2 > 600:
            color = red
            mouse_y += abs(yf2 - 600)
            robot.moveTo(mouse_x, mouse_y, 0)

        out2 = cv2.rectangle(imgout, (400,100),(900,600),color,2)

face_detect(loop, cam, face_model, eye_model)