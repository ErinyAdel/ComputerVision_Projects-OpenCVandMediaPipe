"""
Created on Sun Aug 22 15:56:11 2021
@author: Eriny
"""

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')				 ## Handle The Resolution And Colors Of The Video
saved = cv2.VideoWriter('SavedCameraVideo.avi', fourcc, 20.0, (640,480)) ## 20 Frames Per Seconds, (frameWidth, frameHeight) 

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:        
        ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## Convert Color
        cv2.imshow('Live', frame)

        ## Save Video
        saved.write(frame)
        
        k = cv2.waitKey(1)
        if k == 27:
            break
    else:
        break

cap.release()   ## To Close The Camera
saved.release() ## To 
cv2.destroyAllWindows()