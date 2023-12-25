Change the Color
================


In this activity, you will color the bounding box and age prediction values with different colors for different bands of age group.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10580123/image__41_.png" width = "480" height = "220">
<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10580126/image__39_.png" width = "480" height = "220">


Follow the given steps to complete this activity:


1. Add color to age and bounding box


* Open the main.py file.


* Create a `color` variable and assign it RGB values for white color.


    `color = (255, 255, 255)`


*  Assign different color to different range of age group. 

    `if prediction[0][0] < 80:`

        `color = (255, 0, 255)`

    `if prediction[0][0] < 60:`

        `color = (255, 255, 0)`

    `if prediction[0][0] < 40:`

        `color = (0, 255, 255)`

    `if prediction[0][0] < 20:`


        `color = (255, 0, 0)`


* Use the `color` variable to give color to the `text`.


    `img = cv2.putText(img, str(int(prediction[0][0])), (X, Y), cv2.FONT_HERSHEY_DUPLEX, 1.0, color, 2)`
   
* Use the `color` variable to give color to the `rectangle`.


    `img = cv2.rectangle(img, (X, Y), (X+W, Y+H), color, 1)`
                       
* Save and run the code to check the output.
