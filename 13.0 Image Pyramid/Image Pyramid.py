"""
Created on Wed Aug 25 14:47:22 2021
@author: Eriny
"""

import cv2 as cv

img            = cv.imread('messi.jpeg')
cv.imshow("Level 1 - Original", img)

## Get Quarter of Original Pic {Lost Information From It} --> Save Odd Num & Remove Even
lowResolution  = cv.pyrDown(img)           ## 1/4 {Level 2}
lowResolution2 = cv.pyrDown(lowResolution) ## 1/8 {Level 3}
cv.imshow("Level 2 - Quarter of Original", lowResolution)
cv.imshow("Level 3 - The Quarter From Quarter Of Original", lowResolution2)


## The Resolution will decrease even we back in levels {BECAUSE OF: Lost of many Info}
highResolution = cv.pyrUp(lowResolution2) 
cv.imshow("Back To Level 2", highResolution)

## --------------------------------------------------------------------------------------

copyImg = img.copy()
Layers  = [copyImg]

for i in range(6):
    copyImg = cv.pyrDown(copyImg)
    Layers.append(copyImg)
    cv.imshow(str(i), copyImg)

## ------------------------------

for i in range(6):
    copyImg = cv.pyrUp(copyImg)
    Layers.append(copyImg)
    cv.imshow(str(i), copyImg)
    
    
cv.waitKey(0)
cv.destroyAllWindows()