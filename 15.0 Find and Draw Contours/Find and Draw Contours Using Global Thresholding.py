"""
Created on Thu Aug 26 11:01:26 2021
@author: Eriny
"""

import cv2 as cv 

img = cv.imread('OpenCV_Logo.png')
img = cv.resize(img, (512,280))

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) ## Convert image to gray scale because of using thresholding
_, thresholding = cv.threshold(imgGray, 20, 255 , 0) ## 
contours, hierarchy = cv.findContours(thresholding, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
contours2, _ = cv.findContours(thresholding, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("Numbers of Contours:" + str(len(contours)))
print(contours[0])

cv.imshow("Gray Image", imgGray)

##              src, contours, Contours, Color, FontThickness --> -1 = All Contours, 0 (Any Num From len(contours)) = Index # From Contours
cv.drawContours(img, contours, -1, (255,0,255), 2) ## Draw The Contours On Original Image
cv.drawContours(imgGray, contours2, -1, (255,255,0), 2) ## Draw The Contours On Gray Image

cv.imshow("Image After Drawing", img)
cv.imshow("Gray Image After Drawing", imgGray)

cv.waitKey(0)
cv.destroyAllWindows()