# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:49:44 2021
@author: Eriny
"""


import cv2 as cv

faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade  = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray  = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    
    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
        cv.putText(frame, "Face", (x, y-4), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
    
        eyes = eyeCascade.detectMultiScale(gray, 2.3, 4)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(frame, (ex,ey), (ex+ew,ey+eh), (255,0,0), 5)
            cv.putText(frame, "Eye", (ex, ey-3), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
            
    cv.imshow("Image",frame)
    if cv.waitKey(1) == ord('q'):
        cap.release()
        break

cap.release()
cv.destroyAllWindows()
