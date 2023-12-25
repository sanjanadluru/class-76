from cvzone.FaceDetectionModule import FaceDetector
import cv2
import numpy as np
from keras.models import load_model

cap = cv2.VideoCapture(0)

detector = FaceDetector()

ageDetectionModel = load_model('age_model_50epochs.h5', compile=False)

while True:
    try:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        
        img, bboxs = detector.findFaces(img, draw=False)

        if bboxs: 
            for box in bboxs:
                X, Y, W, H = box['bbox']

                croppedImg = img[Y:Y+H, X:X+W]
                resizedImg = cv2.resize(croppedImg, (200, 200))
                resizedImg = np.array([resizedImg])
                
                prediction = ageDetectionModel.predict(resizedImg)

                # Create a color variable and give it white color 
                

                # Check if prediction[0][0] i.e age is less then 20 and assign a color to color variable
                
                # Check if prediction[0][0] i.e age is less then 40 and assign a color to color variable
                
                # Check if prediction[0][0] i.e age is less then 60 and assign a color to color variable
                
                # Check if prediction[0][0] i.e age is less then 80 and assign a color to color variable
                

                # Use color variable to give color to the text
                img = cv2.putText(img, str(int(prediction[0][0])), (X, Y), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
                 
                # Use color variable to give color to the rectangle
                img = cv2.rectangle(img, (X, Y), (X+W, Y+H), (255, 255, 255), 1)
             
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Exception", e)

cv2.destroyAllWindows()
