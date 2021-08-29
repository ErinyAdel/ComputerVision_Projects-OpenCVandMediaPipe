"""
Created on Mon Aug 23 10:50:26 2021
@author: Eriny
"""

## HSV --> Stands for: Hue, Saturation, Value.     [Chack HSV.png Image]

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
    

cv.namedWindow("Trackbar")
cv.createTrackbar('Lower H', "Trackbar", 0, 255, nothing)
cv.createTrackbar('Lower S', "Trackbar", 0, 255, nothing)
cv.createTrackbar('Lower V', "Trackbar", 0, 255, nothing)
cv.createTrackbar('Upper H', "Trackbar", 255, 255, nothing)
cv.createTrackbar('Upper S', "Trackbar", 255, 255, nothing)
cv.createTrackbar('Upper V', "Trackbar", 255, 255, nothing)


while True:
    frame = cv.imread('balls2.png')
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos('Lower H', 'Trackbar')
    u_h = cv.getTrackbarPos('Upper H', 'Trackbar')
    l_s = cv.getTrackbarPos('Lower S', 'Trackbar')
    u_s = cv.getTrackbarPos('Upper S', 'Trackbar')
    l_v = cv.getTrackbarPos('Lower V', 'Trackbar')
    u_v = cv.getTrackbarPos('Upper V', 'Trackbar')
    
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    
    mask = cv.inRange(hsv, lower, upper) ## [Threshold the HSV image] Whole image is black except pixels with this color range
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow("res", res)
    cv.imshow("mask", mask)
    cv.imshow("frame", frame)
    
    key = cv.waitKey(1)
    if key == 27:
        break
    

cv.destroyAllWindows()