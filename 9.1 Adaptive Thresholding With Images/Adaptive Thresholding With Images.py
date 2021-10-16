"""
Created on Mon Aug 23 13:45:32 2021
@author: Eriny
"""

import cv2 as cv

img = cv.imread('sudoku.jpg', 0)
cv.imshow("Original", img)
_, binaryTH = cv.threshold(img, 55, 317, cv.THRESH_BINARY) ## X --> Light in the image is irregular (Not gradient)
cv.imshow("Binary Thresholding", binaryTH)


_, meanCTH = cv.adaptiveThreshold(img, 317, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 111, 2)
cv.imshow("Mean C Thresholding", meanCTH)


cv.waitKey(0)
cv.destroyAllWindows()