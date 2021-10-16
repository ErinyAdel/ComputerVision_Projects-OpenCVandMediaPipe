# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:22:15 2021
@author: Eriny
"""

import dlib
import cv2 

detector  = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    ## Detect The Face To Detect Its Landmarks
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        print(face)
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        ## Get The Landmarks Of Detected Face
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            print(x,y)
            cv2.circle(frame, (x,y), 2, (255,255,0), -1)
        
    ## Display The Frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == 27:
        cap.release()
        break
        
cap.release()
cv2.destroyAllWindows()
