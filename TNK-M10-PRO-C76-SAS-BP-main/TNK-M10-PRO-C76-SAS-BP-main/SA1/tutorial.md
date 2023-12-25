Capture Video and Detect the Faces
===============================

In this activity, you will capture the video feed and detect the faces.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/8241f76f-20f2-4c6f-99b8-a3b8862088c8.gif" width = "480" height = "220">



Follow the given steps to complete this activity:


1. Capture the Video


* Open the main.py file.


* Import `Face Detection, cv2 and NumPy` library .


    `from cvzone.FaceDetectionModule import FaceDetector`


    `import cv2`


    `import numpy as np`


* Capture the webcam video feed.


    `cap = cv2.VideoCapture(0)`




 *   Read the images frame by frame from the captured video and store it in the img variable.


    `success, img = cap.read()`


* Store the flipped video frames using `cv2.flip(img, 1)`.


    `img = cv2.flip(img, 1)`


* Detect the face using FaceDetector and store the bounded boxes.


    `detector = FaceDetector()`


    `img, bboxs = detector.findFaces(img, draw=False)`


* Check if `bounding box` exits and traverse through each box to store coordinates and dimensions.


    `if bboxs:`


    `for box in bboxs:`
    `    X, Y, W, H = box['bbox']`


* Draw a rectangle on the detected face using `X, Y, W, H`.


    `img = cv2.rectangle(img, (X, Y), (X+W, Y+H), (255, 255, 255), 1)`


* Display the image.    


    `cv2.imshow("Image", img)`x
         
* Save and run the code to check the output.
