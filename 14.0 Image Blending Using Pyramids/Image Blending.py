"""
Created on Wed Aug 25 22:30:20 2021
@author: Eriny
"""


import cv2 as cv
import numpy as np

img1 = cv.imread('apple_307x307.jpg')
img2 = cv.imread('orange_307x307.jpg')

## Insure the size of two sizes is equal
print(img1.shape)
print(img2.shape)

##                 All Rows, From 0 To 307/2 - All Rows, From 153 To End (307)
combain = np.hstack((img1[:, :153], img2[:, 153:]))
cv.imshow("Combained Without Blending", combain)

## Generate Gaussian Pyramid For First Image
img1Copy = img1.copy()
gaussianList1 = [img1Copy]

for i in range(6):
    img1Copy = cv.pyrDown(img1Copy)
    gaussianList1.append(img1Copy)
    

## Generate Gaussian Pyramid For Second Image
img2Copy = img2.copy()
gaussianList2 = [img2Copy]

for i in range(6):
    img2Copy = cv.pyrDown(img2Copy)
    gaussianList2.append(img2Copy)
    
    
## Generate Laplacian Pyramid For First Image
img1Copy = gaussianList1[5]
laplacianList1 = [img1Copy]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gaussianList1[i])
    laplacian = cv.subtract(gaussianList1[i-1], gaussianExtended)
    laplacianList1.append(laplacian)


## Generate Laplacian Pyramid For Second Image
img2Copy = gaussianList2[5]
laplacianList2 = [img2Copy]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gaussianList2[i])
    laplacian = cv.subtract(gaussianList2[i-1], gaussianExtended)
    laplacianList2.append(laplacian)


## Add Left & Right Halves in Each Level
imgsPyramidList = []
for img1Laplacian, img2Laplacian in zip(laplacianList1, laplacianList2):
    cols, rows, ch = img1Laplacian.shape
    laplacian = np.hstack((img1Laplacian[:, 0:int(cols/2)], img2Laplacian[:, int(cols/2):]))
    imgsPyramidList.append(laplacian)
    
## Reconstruct
imgsConstruct = imgsPyramidList[0]
#cv.imshow("Combained Before Increasing The Size", imgsConstruct) 

for i in range(1, 6):
    imgsConstruct = cv.pyrUp(imgsConstruct)  ## Increasing The Size -- But Blurring
    imgsConstruct = cv.add(imgsPyramidList[i], imgsConstruct) ## Remove Blurring
    
cv.imshow("Combained After Increasing The Size", imgsConstruct) 

cv.waitKey(0)
cv.destroyAllWindows()

