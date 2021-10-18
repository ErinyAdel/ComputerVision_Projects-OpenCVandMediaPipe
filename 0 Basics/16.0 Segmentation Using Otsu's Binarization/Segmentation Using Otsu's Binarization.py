"""
Created on Fri Aug 27 19:35:31 2021
@author: Eriny
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('noisy.png',0)
#cv.imshow("Original", img)

## Thresholding
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#cv.imshow("Threshold", th1)

## Otsu's thresholding
_,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#cv.imshow("Out's Threshold", th2)

## Otsu's thresholding after Gaussian filtering
gaussianBlur = cv.GaussianBlur(img,(5,5),0)
#cv.imshow("Gaussian Blur", gaussianBlur)
_,th3 = cv.threshold(gaussianBlur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Plot all the images and their histograms
images = [img         , 0, th1,
          img         , 0, th2,
          gaussianBlur, 0, th3]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding (v=255)",
          'Gaussian Filtered Image','Histogram',"Otsu's Thresholding (v=255)"]

## subplot param: rows, cols, index
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.savefig('Saved plt.png')
plt.show()

cv.imshow("Result", cv.imread('Saved plt.png'))

cv.waitKey(0)
cv.destroyAllWindows()




"""
Trace For (for-loop)
-------------------
0::   
1, 0
0

2, 0
1

3, 2
2
-------------------
1::
4, 3
3

5, 3
4

6, 5
5
-------------------
2::
7, 6
6

8, 6
7

9, 8
8
-------------------
"""