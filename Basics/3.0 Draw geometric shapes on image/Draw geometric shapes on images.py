"""
Created on Sun Aug 22 17:51:35 2021
@author: Eriny
"""

import numpy as np
import cv2

img = np.zeros([512,512,3], np.uint8) # 512x512 Matrix (Include 3x3 Matrices) Of Zeros --> Black
print(img)
cv2.imshow('Original', img)
##              src, start, end, color, thickness
img  = cv2.line(img, (512,256), (256,256), (0,0,255), 4)
cv2.imshow('Line', img)
img = np.zeros([512,512,3], np.uint8)

img2 = cv2.arrowedLine(img, (256,0), (256,256), (0,0,255), 5)
cv2.imshow('Arrowed Line', img2)
img = np.zeros([512,512,3], np.uint8)

img3 = cv2.rectangle(img, (0,0), (256,256), (0,255,0), 3)
cv2.imshow('Rectangle', img3)
img = np.zeros([512,512,3], np.uint8)

img31 = cv2.rectangle(img, (256,256), (512,512), (0,255,0), -1)
cv2.imshow('Hollow Rectangle', img31)
img = np.zeros([512,512,3], np.uint8)

##                src, center, radius, color, thickness
img4 = cv2.circle(img, (256,256), 120, (255,0,0), 2)
cv2.imshow('Circle', img4)
img = np.zeros([512,512,3], np.uint8)

img41 = cv2.circle(img, (256,256), 120, (255,0,0), -1)
cv2.imshow('Hollow Circle', img41)
img = np.zeros([512,512,3], np.uint8)

pts = np.array([[10,50],[100,10],[120,70],[200,80],[30,212]], np.int32)
##                   img, pts, isClosed, color
img5 = cv2.polylines(img, [pts], True, (0,255,255))
cv2.imshow('Irregular Shape', img5)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()