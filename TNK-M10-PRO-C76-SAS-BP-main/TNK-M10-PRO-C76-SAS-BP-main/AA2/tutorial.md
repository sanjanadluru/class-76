Debug the Code
================


In this activity, you will debug the code to remove extra detection rectangles and fix the position of the bounded box in a video.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10580191/pasted-from-clipboard.png" width = "480" height = "220">


Follow the given steps to complete this activity:


1. Debug the code


* Open the main.py file.


* Capture the video fed from the webcam.


    `cap = cv2.VideoCapture("v1.mp4")`


* Remove the extra face detection rectangles by setting the value of `draw` to `False`.


    `img, bboxs = detector.findFaces(img, draw=False)`


* Fix the location of the bounded box.


    `X, Y, W, H = box['bbox']`
           
* Save and run the code to check the output.