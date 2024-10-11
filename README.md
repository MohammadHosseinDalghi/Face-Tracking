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
5. I also put the Jupyter format for better experience.

## Requirements
- Python 3.10.11
- OpenCV (`cv2`)
- PyAutoGUI (`pyautogui`)
- A webcam

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/MohammadHosseinDalghi/Face-Tracking.git
    cd Face-Tracking
    ```

2. Install the required Python libraries:
    ```bash
    pip install opencv-python pyautogui
    ```

3. Ensure that the Haar Cascade XML files for face and eye detection are in the project directory:
    - `haarcascade_frontalface_default.xml`
    - `haarcascade_eye.xml`

4. Run the Python script:
    ```bash
    python face_eye_detection.py
    ```
