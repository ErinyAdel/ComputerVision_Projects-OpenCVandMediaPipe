# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:24:36 2021
@author: Eriny
"""

"""
Algorithms:
    
1. Gift wrapping, a.k.a. Jarvis march — O(nh)
2. Graham scan — O(nlogn)
3. Chan’s algorithm — O(nlogh)
4. Sklansky (1982) — O(nlogn) ( OpenCV uses this algorithm)
"""

import cv2

img = cv2.imread('cars.png')
img = cv2.resize(img, (650,500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thr = cv2.threshold(gray, 50, 255, 0)
contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

## Find and draw 'Convex Hull' for each contour
for i in range(len(contours)):
    conv_hull = cv2.convexHull(contours[i])
    cv2.drawContours(img, [conv_hull], -1, (255,0,0), 2)

cv2.imshow("ConvexHull", img)
cv2.waitKey(0)
cv2.destroyAllWindows()