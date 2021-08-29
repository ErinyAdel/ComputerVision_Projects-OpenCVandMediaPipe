"""
Created on Tue Aug 24 23:42:56 2021
@author: Eriny
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Lenna_512x512.png', -1)
cv.imshow("Image", img)

## matplotlib Lib. show images in "BGR"
#plt.imshow(img) ## BGR

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) ## Convert From BGR To RGB
plt.imshow(img) ## RGB

cv.waitKey(0)
cv.destroyAllWindows()