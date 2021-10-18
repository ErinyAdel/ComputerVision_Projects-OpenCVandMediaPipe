# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:41:44 2021
@author: Eriny
"""

"""
Page segmentation modes:
• Orientation and script detection (OSD) only                       ==> --psm 0
• Automatic page segmentation, but no OSD/OCR                       ==> --psm 1
• Automatic page segmentation, with OSD                             ==> --psm 2
• Fully automatic page segmentation, but no OSD                     ==> --psm 3
• Assume a single column of text of variable sizes                  ==> --psm 4
• Assume a single uniform block of vertically aligned text          ==> --psm 5
• Assume a single uniform block of text                             ==> --psm 6
• Treat the image as a single text line                             ==> --psm 7
• Treat the image as a single word                                  ==> --psm 8
• Treat the image as a single word in a circle                      ==> --psm 9 
• Treat the image as a single character                             ==> --psm 10
• Sparse text. Find as much text as possible in no particular order ==> --psm 11
• Sparse text with OSD                                              ==> --psm 12
• Raw line. Treat the image as a single text line bypassing hacks that are Tesseract-specific.
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test3.jpg')
img = cv2.resize(img, None, fx=0.5, fy=0.3)

## Pre-processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 30) ## Lighting

config = '--psm 6' ## test1.jpg==> --psm 3 + psm 6, test3==> --psm 6
target = pytesseract.image_to_string(adaptive_thr, config=config) ## lang='chi_sim' --> For Chinaese language

cv2.imshow("Gray", gray)
cv2.imshow("Adaptive Threshold", adaptive_thr)
cv2.waitKey(0)
cv2.destroyAllWindows()