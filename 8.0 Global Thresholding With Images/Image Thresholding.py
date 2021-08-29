"""
Created on Mon Aug 23 12:57:53 2021
@author: Eriny
"""

import cv2 as cv

img = cv.imread('GradientBlackandWhite_256x256.png')
##                         src, th, Max (255), type   -   
_, binaryTH        = cv.threshold(img, 55, 256, cv.THRESH_BINARY)      ## [Pixel <= th -> Black, Pixel > th -> White]
_, binaryInverseTH = cv.threshold(img, 200, 256, cv.THRESH_BINARY_INV) ## [Pixel <= th -> White, Pixel > th -> Black]
_, truncTH         = cv.threshold(img, 60, 256, cv.THRESH_TRUNC)       ## [Pixel <= th -> Same , Pixel > th -> th]
_, toZeroTH        = cv.threshold(img, 127, 256, cv.THRESH_TOZERO)     ## [Pixel <= th -> 0    , Pixel > th -> Same]
_, toZeroInverseTH = cv.threshold(img, 127, 256, cv.THRESH_TOZERO_INV) ## [Pixel <= th -> Same , Pixel > th -> 0]


cv.imshow("Original Image", img)
cv.imshow("Binary Threshold", binaryTH)
cv.imshow("Inverse Binary Threshold", binaryInverseTH)
cv.imshow("Trunc Threshold", truncTH)
cv.imshow("To Zero Threshold", toZeroTH)
cv.imshow("To Zero Inverse Threshold", toZeroInverseTH)

cv.waitKey(0)
cv.destroyAllWindows()