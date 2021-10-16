"""
Created on Fri Aug 27 19:22:39 2021
@author: Erimy
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Lenna_512x512.png', 0) ## 0 --> Gray Scale
cv.imshow("Original Image [Gray Scale]", img)
## Histogram
##                 src, channels, mask, histSize, ranges)
hist = cv.calcHist(img, [0], None, [255], [0,255]) ## Number of channels = [0] Because We Use Gray Scale)
plt.plot(hist)
plt.show()


img = cv.imread('Lenna_512x512.png') ## RGB Scale
cv.imshow("Original Image [RGB Scale]", img)
color = ('b','g','r')

for i, col in enumerate(color): ## enumerate --> b = 0, g = 1, r = 2
    hist = cv.calcHist(img,[i],None,[255],[0,255]) ## Number of channels = [i] Because We Use RGB Scale)
    plt.plot(hist,color = col)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()