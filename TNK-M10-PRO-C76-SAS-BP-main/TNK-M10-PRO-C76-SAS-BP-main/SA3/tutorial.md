Predict the Age
================

In this activity, you will predict the ages in real time using the trained tested model.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10572923/Slide_6-02.gif" width = "480" height = "220">




Follow the given steps to complete this activity:


1. Predict the age


* Open the main.py file.


* Load the age detection model.


    `ageDetectionModel = load_model('age_model_50epochs.h5', compile=False)`


* Predict the age of the resized images using age detection model and save it in `prediction` variable.


    `prediction = ageDetectionModel.predict(resizedImg)`


* Display the predicted age using the .putText() method..


    `img = cv2.putText(img, str(int(prediction[0][0])), (X, Y), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)`
               
* Save and run the code to check the output.


