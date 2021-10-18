"""
Created on Sun Aug 22 23:40:06 2021
@author: Eriny
"""

import cv2
import numpy as np

##               y,x
img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
cv2.imshow("Image 1", img1)

img2 = np.full((250,500,3), 255, np.uint8)
img2 = cv2.rectangle(img2, (0,0), (250,250), (0,0,0), -1)
cv2.imshow("Image 2", img2)

bitAND   = cv2.bitwise_and(img1,img2)
cv2.imshow("AND", bitAND)
bitOR    = cv2.bitwise_or(img1,img2)
cv2.imshow("OR", bitOR)
bitXOR   = cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR", bitXOR)
bitNOT_1 = cv2.bitwise_not(img1)
cv2.imshow("NOT For Img1", bitNOT_1)
bitNOT_2 = cv2.bitwise_not(img2)
cv2.imshow("NOT For Img2", bitNOT_2)

cv2.waitKey(0)
cv2.destroyAllWindows()