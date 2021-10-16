# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:15:49 2021
@author: Eriny
"""

import dlib
import cv2 

detector  = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    ## Detect The Face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        #print(face)
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255), 2)
    
    ## Display The Frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        break
        
cap.release()
cv2.destroyAllWindows()