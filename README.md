# Face and Eye Detection with Mouse Control

This project demonstrates face and eye detection using OpenCV's Haar Cascade models to track a user's face and eyes in real-time via a webcam feed. Additionally, the PyAutoGUI library is used to control the mouse pointer based on the user's head movement within a specified region.

## Features
- Real-time face and eye detection using OpenCV.
- Control mouse movement based on head position.
- Customizable region for face detection that triggers mouse pointer adjustments.

## How It Works
1. The webcam captures the video feed, which is processed frame by frame.
2. The face is detected using the `haarcascade_frontalface_default.xml` model, and eyes are detected using the `haarcascade_eye.xml` model.
3. The mouse pointer moves when the detected face moves out of the predefined region (center of the screen). 
   - If the face moves too far left, right, up, or down, the mouse pointer will follow the direction of the movement.
4. The program flips the webcam feed to make it behave like a mirror.


