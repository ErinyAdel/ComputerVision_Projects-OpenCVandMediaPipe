"""
Created on Wed Aug 25 10:04:50 2021
@author: Eriny
"""

## Morphological Transformations: Works on Black & White Images Only

import cv2 as cv
import numpy as np

img = cv.imread('balls.png', 0)
_, mask = cv.threshold(img, 240, 390, cv.THRESH_BINARY_INV) ## [Pixel <= th -> White, Pixel > th -> Black]

kernel = np.ones((3,3), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=2) ## Increase Size Of Objects [Dilation Size ∝ Num of Iteration] -- Good
erosion  = cv.erode(mask, kernel, iterations=2)  ## Decrease Size Of Objects [Pixel in Kernel < 1 --> It Eroded] -- Not Good

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=3)  ## Erosion  THEN  Dilation
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=2) ## Dilation THEN  Erosion

cv.imshow("Original", img)
cv.imshow("Mask", mask)
cv.imshow("After Dilation", dilation)
cv.imshow("After Erosion", erosion)
cv.imshow("After Opening", opening)
cv.imshow("After Closing", closing)

cv.waitKey(0)
cv.destroyAllWindows()