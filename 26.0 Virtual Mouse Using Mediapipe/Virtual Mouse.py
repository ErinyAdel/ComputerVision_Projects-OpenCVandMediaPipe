# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:33:51 2021
@author: Eriny
"""

import cv2
import mediapipe as mp
import numpy
import autopy

cap = cv2.VideoCapture(0)
initHand = mp.solutions.hands
mainHand = initHand.Hands()

hand_draw = mp.solutions.drawing_utils

screenWidth, screenHeight = autopy.screen.size()
pX, pY = 0, 0 ## Previous x, y location
cX, cY = 0, 0 ## Current  x, y location 
    
def handLandmarks(color_img):
    