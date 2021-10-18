# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:31:07 2021

@author: 20122
"""

import cv2
import datetime

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
## Default Size
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  ## cv2.CAP_PROP_FRAME_WIDTH  -> 3
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) ## cv2.CAP_PROP_FRAME_HEIGHT -> 4

##      ID,Value
cap.set(3, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

while(cap.isOpened()):
    _, frame = cap.read()
    
    font     = cv2.FONT_HERSHEY_SIMPLEX
    
    text     = "Width: " + str(cap.get(3)) + '  Height: ' + str(cap.get(4))
    currDate = str(datetime.datetime.now())
    
    frame = cv2.putText(frame, text, (10,30), font, 1, (0,255,255), 1)
    frame = cv2.putText(frame, currDate, (10,60), font, 1, (0,255,255), 1)    
    cv2.imshow('Live', frame)

    if cv2.waitKey(10) == 27:
      break

cap.release()
cv2.destroyAllWindows()