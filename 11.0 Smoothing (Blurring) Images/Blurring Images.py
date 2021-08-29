"""
Created on Wed Aug 25 10:41:06 2021
@author: Eriny
"""

## Remove the noises from images using diverse linear filter [Conventional Concept]
## NOTE: Types of "Linear Filter" --> 1. Low-path Filter : To Remove Noise From Images (Enhancement) 
##                                    2. High-path Filter: To Detect Edges Of Images 


import cv2 as cv

img2 = cv.imread('Lenna_512x512.png') 
img2 = cv.imread('balloons_noisy.png')
cv.imshow("Original 2", img2)

averaging = cv.blur(img2, (2,2)) ## Mean For Pixels -- [Filter ↑ = (Noises ↓ + Blur ↑)]
cv.imwrite("After Averaging 2.jpg", averaging) 
cv.imshow("Averaging 2", averaging)

gaussian = cv.GaussianBlur(img2, (3,3), 0) 
cv.imwrite("After Gaussian 2.jpg", gaussian) 
cv.imshow("Gaussian 2", gaussian)

median = cv.medianBlur(img2, 3) ## For salt and paper [Iamges which have many white points as pixels] 
cv.imwrite("After Mdian 2.jpg", median)
cv.imshow("Median 2", median)

bilateral = cv.bilateralFilter(img2, 70, 0, 0) ## For the edges of the images (src, d, sigmaColor, sigmaSpace)
cv.imwrite("After Bilateral.jpg", bilateral)
cv.imshow("Bilateral", bilateral)

## -----------------------------------------------------------------------------------------------------------

img = cv.imread('pixelated.jpg') 
cv.imshow("Original", img)

averaging = cv.blur(img, (2,2)) ## Mean For Pixels -- [Filter ↑ = (Noises ↓ + Blur ↑)]
cv.imwrite("After Averaging.jpg", averaging) 
cv.imshow("Averaging", averaging)

gaussian = cv.GaussianBlur(img, (3,3), 0) 
cv.imwrite("After Gaussian.jpg", gaussian) 
cv.imshow("Gaussian", gaussian)

median = cv.medianBlur(img, 3) ## For salt and paper [Iamges which have many white points as pixels] 
cv.imwrite("After Mdian.jpg", median)
cv.imshow("Median", median)

bilateral = cv.bilateralFilter(img, 9, 0, 0) ## For the edges of the images (src, d, sigmaColor, sigmaSpace)
cv.imwrite("After Bilateral.jpg", bilateral)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
cv.destroyAllWindows()