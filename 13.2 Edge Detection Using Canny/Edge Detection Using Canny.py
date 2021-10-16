"""
Created on Wed Aug 25 13:57:26 2021
@author: Eriny
"""

"""
Canny Edgy Detection: 
    1. Converts image to gray scale by using equation: y = 0.299R + 0.587G + 0.114B
    2. Removes the noises from the image by using "Gaussian filter"
    3. Use SobelX, SobelY to get the edges in two directions and combine them by using equation: Edge_Gradient(G) = Sqr(Gx^2 + Gy^2)    
    4. Apply Non-maximum suppression to make the edges thin by using equation: Angle(Θ) = tan ^-1 (Gy / Gx)
    5. Hysteresis thresholding to connect the strong edges and ignore other
"""

import cv2 as cv
import numpy as np

img = cv.imread('messi.jpeg', 3)
canny = cv.Canny(img, 100, 200)

cv.imshow("Original", img)
cv.imshow("Canny Edge Detection", canny)

cv.waitKey(0)
cv.destroyAllWindows()