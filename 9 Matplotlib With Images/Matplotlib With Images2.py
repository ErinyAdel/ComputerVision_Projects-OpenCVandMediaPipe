"""
Created on Tue Aug 24 23:52:20 2021
@author: Eriny
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('GradientBlackandWhite_256x256.png', 0)
_, binaryTH        = cv.threshold(img, 55, 256, cv.THRESH_BINARY)      ## [Pixel <= th -> Black, Pixel > th -> White]
_, binaryInverseTH = cv.threshold(img, 200, 256, cv.THRESH_BINARY_INV) ## [Pixel <= th -> White, Pixel > th -> Black]
_, truncTH         = cv.threshold(img, 60, 256, cv.THRESH_TRUNC)       ## [Pixel <= th -> Same , Pixel > th -> th]
_, toZeroTH        = cv.threshold(img, 127, 256, cv.THRESH_TOZERO)     ## [Pixel <= th -> 0    , Pixel > th -> Same]
_, toZeroInverseTH = cv.threshold(img, 127, 256, cv.THRESH_TOZERO_INV) ## [Pixel <= th -> Same , Pixel > th -> 0]

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
imgs   = [img, binaryTH, binaryInverseTH, truncTH, toZeroTH, toZeroInverseTH]

for i in range(6): ## From 0 To 5
    ##         Rows, Columns, Iterations
    plt.subplot(2, 3, i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([]) ## To remove x-aix & y-axis numbers
    
    
plt.show()