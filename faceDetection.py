import cv2
from pynput.keyboard import Key, Controller

keyboard = Controller()
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
isPause = False
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) > 0:
        if isPause:
            isPause = False
            with keyboard.pressed(Key.alt):
                keyboard.press(Key.tab)
            keyboard.release(Key.alt)
            ##keyboard.press('k')
    else:
        if isPause:
            pass
        else:
            isPause = True
            #keyboard.press('k')
            with keyboard.pressed(Key.alt):
                keyboard.press(Key.tab)
            keyboard.release(Key.alt)
    print(isPause)
