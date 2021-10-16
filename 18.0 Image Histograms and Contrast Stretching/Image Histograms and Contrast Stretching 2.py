"""
Created on Fri Aug 27 18:52:33 2021
@author: Eriny
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Lenna_512x512.png')
cv.imshow("Original Image", img)
## Histogram
plt.hist(img.ravel(), 255, [0,255])
#plt.show()
b, g, r = cv.split(img)
cv.imshow("Red",r)
cv.imshow("Green",g)
cv.imshow("Blue",b)
## Histogram
plt.hist(r.ravel(), 255, [0,255])
#plt.show()
plt.hist(g.ravel(), 255, [0,255])
#plt.show()
plt.hist(b.ravel(), 255, [0,255])
#plt.show()

plt.show() ## For 4 together


cv.waitKey(0)
cv.destroyAllWindows()