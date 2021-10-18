# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:01:15 2021
@author: Eriny
"""
import cv2
import mediapipe as mp

## Face Mesh
face_mesh_mp = mp.solutions.face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
        
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = face_mesh_mp.process(rgb)
    
    h, w, _ = img.shape
    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            #print(pt1)
            x = int(pt1.x * w)
            y = int(pt1.y * h)
            cv2.circle(img, (x,y), 2, (0, 0, 0), -1)
        
    cv2.imshow("Frame",img)
    if cv2.waitKey(1) == 27:
        cap.release()
        break

cv2.destroyAllWindows()
cap.release()
