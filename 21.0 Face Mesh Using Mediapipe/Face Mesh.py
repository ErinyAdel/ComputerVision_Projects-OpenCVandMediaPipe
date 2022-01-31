# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:46:31 2021
@author: Eriny
"""

import cv2
import mediapipe as mp

img = cv2.imread('faces2.jpg')
h, w, _ = img.shape

import numpy as np
black_img = np.zeros([h,w,3], np.uint8)

## Face Mesh
face_mesh_mp = mp.solutions.face_mesh.FaceMesh(max_num_faces=10)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = face_mesh_mp.process(rgb)
num_of_face  = 0
for facial_landmarks in result.multi_face_landmarks:
    print('MMM')
    for i in range(0, 468):
        pt1 = facial_landmarks.landmark[i]
        #print(pt1)
        x = int(pt1.x * w)
        y = int(pt1.y * h)
        cv2.circle(img, (x,y), 2, (100, 100, 0), -1)
        cv2.circle(black_img, (x,y), 2, (0,100,0), -1)
    num_of_face += 1
        
cv2.imshow("Frame", img)
cv2.imshow("Frame2", black_img)
print(num_of_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
        