# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:41:44 2021
@author: Eriny
"""

"""
Pagesegmode values are: 0 - Orientation and Script Detection (OSD) only.

• Automatic page segmentation, but no OSD/OCR              ==> --psm 1
• Automatic page segmentation, with OSD                    ==> --psm 2
• Fully automatic page segmentation, but no OSD            ==> --psm 3
• Assume a single column of text of variable sizes         ==> --psm 4
• Assume a single uniform block of vertically aligned text ==> --psm 5
• Assume a single uniform block of text                    ==> --psm 6
• Treat the image as a single text line                    ==> --psm 7
• Treat the image as a single word                         ==> --psm 8
• Treat the image as a single word in a circle             ==> --psm 9 
• Treat the image as a single character                    ==> --psm 10
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test1.jpg')
#img = cv2.resize(img, None, fx=0.5, fy=0.3)

## Pre-processing
averaging = cv2.blur(img, (2,2))
gray = cv2.cvtColor(averaging, cv2.COLOR_BGR2GRAY)
adaptive_thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 20) ## Lighting

config = '--psm 3' ## test1.jpg==> --psm 3 + psm 6, test3==> --psm 6
text = pytesseract.image_to_string(img, config=config, lang="eng")

cv2.imshow("Gray", gray)
cv2.imshow("Adaptive Threshold", adaptive_thr)
k = cv2.waitKey(0)
cv2.destroyAllWindows()