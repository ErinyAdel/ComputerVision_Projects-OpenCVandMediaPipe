"""
Created on Sun Aug 29 13:20:31 2021
@author: Eriny
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('barcelona.jpeg',0)
imgCopy = img.copy()
searchImg = cv.imread('Search For Messi.jpeg',0)

w, h = searchImg.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = imgCopy.copy()
    method = eval(meth)
    
    ## Apply template Matching
    res = cv.matchTemplate(img,searchImg,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    
    ## If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum. Else, take maximum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.savefig('.\\Saved Plots\\'+str(method)+'.png')
    plt.show()