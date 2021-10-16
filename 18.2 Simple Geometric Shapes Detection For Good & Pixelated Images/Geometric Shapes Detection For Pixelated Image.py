"""
Created on Sat Aug 28 19:04:36 2021
@author: Eriny
"""

import cv2 as cv
import numpy as np

font = cv.FONT_ITALIC

img = cv.imread('Geometric Shapes 2.jpg') 
imgCopy = img.copy()
cv.imshow("Original", img)

imgGray     = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, mask     = cv.threshold(imgGray, 55, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=3) ## Dilation THEN  Erosion
contours, _ = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 

#cv.imshow("In Gray Scale", imgGray)
cv.imshow("Thresholding", mask)
cv.imshow("closing", closing)

for cnt in contours:
    ## Without using approximation, may be there is noises. So number of contours will be not accurate [Must use approxPolyDP] 
    approx = cv.approxPolyDP(cnt, 0.02*cv.arcLength(cnt,True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 2) ## 0 --> Max dist. between shape and drawed contours.
    ## Get x and y from index 0, 1 from array of cnt/approx to use putText() closed to its shape 
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    ## Detecting the shape form Numbers of contours for each one
    if len(approx) == 3:
        print(approx)
        cv.putText(img, "Triangle", (x,y), font, 0.5, (255,255,255), 1)
        cv.putText(imgCopy, "Triangle", (x,y), font, 0.5, (255,255,255), 1)
    
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio  = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x,y-5), font, 0.5, (255,255,255), 1)
            cv.putText(imgCopy, "Square", (x,y-5), font, 0.5, (255,255,255), 1)
        else:
            cv.putText(img, "Rectangle", (x,y-5), font, 0.5, (255,255,255), 1)
            cv.putText(imgCopy, "Rectangle", (x,y-5), font, 0.5, (255,255,255), 1)
            
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x,y), font, 0.5, (255,255,255), 1)
        cv.putText(imgCopy, "Pentagon", (x,y), font, 0.5, (255,255,255), 1)
        
    elif len(approx) == 6:
        cv.putText(img, "Hexagonal", (x,y-5), font, 0.5, (255,255,255), 1)
        cv.putText(imgCopy, "Hexagonal", (x,y-5), font, 0.5, (255,255,255), 1)
        
    elif len(approx) == 10:
        cv.putText(img, "Star", (x,y), font, 0.5, (255,255,255), 1)
        cv.putText(imgCopy, "Star", (x,y), font, 0.5, (255,255,255), 1)
    
    else:
        cv.putText(img, "Circle", (x,y-5), font, 0.5, (255,255,255), 1)
        cv.putText(imgCopy, "Circle", (x,y-5), font, 0.5, (255,255,255), 1)

cv.imshow("After Detection", img)
cv.imshow("After Detection [Without Contours]", imgCopy)

cv.waitKey(0)
cv.destroyAllWindows()