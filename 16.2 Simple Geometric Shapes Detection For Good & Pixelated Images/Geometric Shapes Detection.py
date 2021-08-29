"""
Created on Thu Aug 26 20:03:40 2021
@author: Eriny
"""

import cv2 as cv

font = cv.FONT_ITALIC

img         = cv.imread('Geometric Shapes.jpg')
#img         = cv.imread("cont_new.png")
imgGray     = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thre     = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 

cv.imshow("In Gray Scale", imgGray)
cv.imshow("Thresholding", thre)

for cnt in contours:
    ## Without using approximation, may be there is noises. So number of contours will be not accurate [Must use approxPolyDP] 
    approx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt,True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 2) ## 0 --> Max dist. between shape and drawed contours.
    ## Get x and y from index 0, 1 from array of cnt/approx to use putText() closed to its shape [Position for writing text]
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #x,y = approx[0][0]
    
    ## Detecting the shape form Numbers of contours for each one
    if len(approx) == 3:
        print(approx)
        cv.putText(img, "Triangle", (x,y), font, 0.5, (0,0,0), 1)
    
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio  = float(w) / h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x,y-5), font, 0.5, (0,0,0), 1)
        else:
            cv.putText(img, "Rectangle", (x,y-5), font, 0.5, (0,0,0), 1)
            
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x,y), font, 0.5, (0,0,0), 1)
        
    elif len(approx) == 6:
        cv.putText(img, "Hexagonal", (x,y-5), font, 0.5, (0,0,0), 1)
        
    elif 6 < len(approx) < 15:
        cv.putText(img, "Ellipse", (x, y-5), font, 0.5, (0,0,0), 1)
        
    elif len(approx) == 10:
        cv.putText(img, "Star", (x,y), font, 0.5, (0,0,0), 1)
    
    else:
        cv.putText(img, "Circle", (x,y-5), font, 0.5, (0,0,0), 1)

cv.imshow("After Detection", img)

cv.waitKey(0)
cv.destroyAllWindows()