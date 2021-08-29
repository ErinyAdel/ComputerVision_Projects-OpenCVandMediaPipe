# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 18:29:41 2021
@author: Eriny
"""

import cv2
import numpy as np

img = np.zeros([512,512,3], np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

height = str(img.shape[0])
width = str(img.shape[1])
channels = img.shape[2]

##                src, text, coordinates, font, fontScale, color, thickness
img = cv2.putText(img,"Width :", (10,40), font, 1, (176,92,8), 1)
img = cv2.putText(img,width, (120,39), font, 0.6, (255,255,255), 1)
img = cv2.putText(img,"Height:", (10,80), font, 1, (176,92,8), 1)
img = cv2.putText(img,height, (120,79), font, 0.6, (255,255,255), 1)
cv2.imshow("Text", img)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()