"""
Created on Sun Aug 22 23:14:21 2021
@author: 20122
"""

import cv2
import numpy as np

img = cv2.imread('apple.jpg')
cv2.imshow("Image",img)
points = []

## --------------------------------------------------------------------------

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue  = img[y,x,0]
        green = img[y,x,1]
        red   = img[y,x,2]
        
        coloredImage = np.zeros((240,240,3),dtype = np.uint8)
        coloredImage[:] = [blue,green,red]
        cv2.imshow("Colored Image",coloredImage)

## --------------------------------------------------------------------------

cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()