"""
Created on Mon Aug 30 10:49:42 2021
@author: Eriny
"""

import cv2 as cv
import numpy as np

img = np.zeros([600,900,3], np.uint8) ## uint8 DataType-Range = 0:255

cv.rectangle(img, (0,0), (900,500), (209,206,0), -1) ## Sky Background
cv.circle(img, (100,100), 40, (0,255,255), -1)       ## Sun
cv.line(img, (700,400), (700,500), (19,69,139), 30)  ## Root of Tree
cv.line(img, (620,450), (620,500), (19,69,139), 25)  ## Root of Tree_2
cv.rectangle(img, (0,500), (900,600), (0,128,0), -1) ## Ground

treeBody = np.array([[600,400], [800,400], [700,120]], np.int32)  ## Branches
treeBody2 = np.array([[560,450], [680,450], [620,250]], np.int32) ## Branches_2
cv.fillPoly(img, [treeBody2], (34,139,34))
cv.fillPoly(img, [treeBody], (34,160,34))

cv.imshow("Garden", img)

cv.waitKey(0)
cv.destroyAllWindows()
