# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:06:42 2021
@author: Eriny
"""

"""
matplotlib ==> RGB Image
opencv     ==> GrayScale Image
"""

import cv2 
#import easyocr
import matplotlib.pyplot as plt
#import imutils

img  = cv2.imread('car1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb  = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
plt.imshow(rgb)

## Bilateral Filter ==> To Reduce The Noises
bilateral_filter = cv2.bilateralFilter(gray, 11, 17, 17) 
rgb = cv2.cvtColor(bilateral_filter, cv2.COLOR_BGR2RGB)
#plt.imshow(rgb)

## Canny ==> Detect The Edges
edge = cv2.Canny(bilateral_filter, 30, 200)
rgb = cv2.cvtColor(edge, cv2.COLOR_BGR2RGB)
#plt.imshow(rgb)

## Contours
keypoints = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours  = 

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()