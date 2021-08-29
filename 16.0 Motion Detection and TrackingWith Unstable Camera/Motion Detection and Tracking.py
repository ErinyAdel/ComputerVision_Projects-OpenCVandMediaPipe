"""
Created on Wed Aug 25 14:35:38 2021
@author: Eriny
"""

## Movement: Difference between two frames

import cv2 as cv
#from tracker import EuclideanDistTracker


kernel    = (5,5)
font      = cv.FONT_HERSHEY_SIMPLEX
frameSize = (1280,700)

cap = cv.VideoCapture('video2.mp4')
fourcc = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
saved  = cv.VideoWriter('Saved.avi', fourcc, 10, frameSize)

## Preprocessing 

_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    ## Get the difference between two frames
    diff        = cv.absdiff(frame1, frame2)
    ## Get the gary sacle                   --> [1. Is faster in processing. 2. Using thresholding needs to it.]
    grayScale   = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    ## Remove Any Nosies (Because of: Difference in lighting in the motion)
    blur        = cv.GaussianBlur(grayScale, kernel, 0)
    ## Get Black and White (Using Thresholding) To Use Contours
    _, th       = cv.threshold(blur, 60, 255, cv.THRESH_BINARY)
    ## Use dilattion to dilate the weak threshold
    dilated     = cv.dilate(th, None, iterations=10)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)    
        if cv.contourArea(contour) < 100:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        
    
    img = cv.resize(frame1, frameSize)
    saved.write(img)
    
    frame1 = cv.resize(frame1, frameSize)
    cv.imshow("Motion Detection", frame1)
    #cv.imshow("Thresholding", th)
    #cv.imshow("Dilation", dilated)
        
    frame1 = frame2
    _, frame2 = cap.read()
    
    if cv.waitKey(60) == 27:
        break
    
    
cv.destroyAllWindows()
cap.release()
saved.release()