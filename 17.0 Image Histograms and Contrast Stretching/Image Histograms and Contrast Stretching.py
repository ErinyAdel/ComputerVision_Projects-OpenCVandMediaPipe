"""
Created on Fri Aug 27 17:34:44 2021
@author: Eriny
"""

## numpy.ravel(): Change 2-D array or Multi-dimensional array into a contiguous flattened array. 
## The returned array has the same data type as the source array or input array. If the input array is a masked array, the returned array will also be a masked array.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((500,500), np.uint8)
cv.imshow("Original Image", img)
## Histogram
plt.hist(img.ravel(), 255, [0,255])
plt.show()

cv.rectangle(img, (0,250), (500,500), (255,0,0), -1)
cv.imshow("Image With Rectangle", img)
plt.hist(img.ravel(), 255, [0,255])
plt.show()


cv.rectangle(img, (0,125), (250,250), (127), -1)
cv.imshow("Image With Another Rectangle", img)
plt.hist(img.ravel(), 255, [0,255])
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()