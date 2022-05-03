import cv2
import os
 
capture = cv2.VideoCapture('Enter the path to your video here') 
 
frameNr = 0
os.mkdir("Frames")

while (True):
    success, frame = capture.read()
    if success:
        cv2.imwrite(os.path.join(os.path.dirname(__file__), "Frames", f"Frame_{frameNr}.jpg"), frame)
    else:
        break
    frameNr = frameNr+1
 
capture.release()