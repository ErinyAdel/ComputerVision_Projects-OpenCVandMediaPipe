"""
Created on Sun Sep 12 16:08:21 2021
@author: 20122
"""

"""

Face Detection: Stage precedes 'Face Recognation' stage
→ The image must be in grayscale
__________________________________________________________________________________________________________

## 1. Selecting Haar-like Features
## 2. Creating  an Integral Image
## 3. Running   AdaBoost Training
## 4. Creating  Classifier Cascades
__________________________________________________________________________________________________________

Integral image instead of original image --> To reduce time complexity
"""

import cv2 as cv

faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    
    gray  = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    
    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
    
    cv.imshow("Image",frame)
    if cv.waitKey(1) == ord('q'):
        cap.release()
        break

cap.release()
cv.destroyAllWindows()
