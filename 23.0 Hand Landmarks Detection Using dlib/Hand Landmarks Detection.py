# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:54:24 2021
@author: Eriny
"""

"""
Documntaion Link: https://google.github.io/mediapipe/solutions/hands#static_image_mode
"""

import cv2
import mediapipe as mp
import time

save_result = cv2.VideoWriter('handlandmarks.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (640, 480))

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
## STATIC_IMAGE_MODE      = False (Default)==> No New Detection while change in input. So it's faster than (True)
## MAX_NUM_HANDS          = 2     (Default)
## MIN_TRACKING_CONFIDENCE= 0.5   (Default) 
## MIN_TRACKING_CONFIDENCE= 0.5   (Default) 
hands    = mp_hands.Hands() 
mp_draw  = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    _, frame = cap.read()
    rgb      = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) ## MediaPipe needs rgb not gray or anything else.
    results  = hands.process(rgb)
    #print(results)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            ## 
            for idd, lm in enumerate(handLms.landmark):
                print(idd,lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(lm, cx, cy)
                if idd == 0:
                    cv2.circle(frame, (cx,cy), 9, (255,0,255), cv2.FILLED)
                    
            ## Fro Drawing Landmarks & Connection Between The Landmarks
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS) 
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (15,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
    
    save_result.write(frame)        
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()