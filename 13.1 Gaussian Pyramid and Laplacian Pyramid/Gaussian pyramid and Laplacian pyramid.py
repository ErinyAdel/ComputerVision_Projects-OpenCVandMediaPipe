"""
Created on Wed Aug 25 21:47:24 2021
@author: Eriny
"""

import cv2 as cv

img            = cv.imread('Lenna_512x512.png')
cv.imshow("Level 1 - Original", img)

imgCopy = img.copy()
gaussianPyramidList = [imgCopy]

for i in range(6):
    imgCopy = cv.pyrDown(imgCopy)
    gaussianPyramidList.append(imgCopy)
    
imgCopy = gaussianPyramidList[5]
cv.imshow("Level 4 [Upper Level - Gaussian Pyramid]", imgCopy)

laplicianPyramidList = [imgCopy]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gaussianPyramidList[i])
    laplician = cv.subtract(gaussianPyramidList[i-1], gaussianExtended) ## Subtract pyrDown - pyrUp
    cv.imshow(str(i), laplician)

cv.waitKey(0)
cv.destroyAllWindows()