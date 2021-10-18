"""
Created on Thu Aug 26 13:33:39 2021
@author: Eriny
"""

## Object Detection From Stable Camera

import cv2

##           W  , H
frameSize = (500,700)
## Detect objects from stable background
objectDetector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40) 


cap = cv2.VideoCapture("hightway.mp4")

## Get the coordinates of all white elements and then remove all small elements that we don't need 

while True:
    ret, frame = cap.read()
    ## Extract Region of interest 
    #height, width, _ = frame.shape
    #print("H = " + str(height) + ", W = " + str(width))
    roi = frame[:800, 3000:3400] 
    
    mask = objectDetector.apply(roi) ## Anything move is white, otherwise is black 
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY) ## [Pixel <= th -> Black, Pixel > th -> White]
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Calculate area and remove small elements 
        area = cv2.contourArea(cnt)
        if area > 100:
            #cv2.drawContours(roi, [cnt], -1, (255,0,0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x+w, y+h), (255,0,0), 2)

        
    frame = cv2.resize(frame, frameSize)
    roi = cv2.resize(roi, frameSize)
    mask = cv2.resize(mask, frameSize)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("roi", roi)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    

cap.release()
cv2.destroyAllWindows()