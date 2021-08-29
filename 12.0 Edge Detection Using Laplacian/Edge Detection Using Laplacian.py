"""
Created on Wed Aug 25 13:15:51 2021
@author: Eriny
"""

import cv2 as cv
import numpy as np

img = cv.imread('messi.jpeg')
cv.imshow("Original", img)

##                 src, ddepth (filter), kernelSize
lap = cv.Laplacian(img, -1, ksize=3)
cv.imshow("Laplacian -1 Filter", lap)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
cv.imshow("Laplacian 64F", lap)

lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian 64F After Set Absolute (Remove Nosies)", lap)

cv.waitKey(0)
cv.destroyAllWindows()