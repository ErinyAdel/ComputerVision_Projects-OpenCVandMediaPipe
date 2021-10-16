"""
Created on Wed Aug 25 13:43:00 2021
@author: Eriny
"""

import cv2 as cv
import numpy as np

img = cv.imread('messi.jpeg')
#img = cv.imread('sudoku.jpg')
cv.imshow("Original", img)

sobelX = cv.Sobel(img, cv.CV_32F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_32F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

cv.imshow("Sobel X", sobelX)
cv.imshow("Sobel Y", sobelY)

combine = cv.bitwise_or(sobelX, sobelY)
cv.imshow("Sobel XY", combine)

cv.waitKey(0)
cv.destroyAllWindows()