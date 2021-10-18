"""
Created on Sun Aug 22 23:29:52 2021
@author: Eriny
"""

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Image",img)
points = []

## --------------------------------------------------------------------------

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 10, (255,0,0), -1)
        points.append((x,y))
        if(len(points) >= 2):
            ##            Last Point, Before Last Point
            cv2.line(img, points[-1], points[-2], (0,255,255))
        cv2.imshow("Image",img)

## --------------------------------------------------------------------------

cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()