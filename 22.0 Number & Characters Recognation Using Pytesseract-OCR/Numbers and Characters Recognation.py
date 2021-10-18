# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:09:55 2021
@author: Eriny
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
img_h, img_w, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
print(boxes)
for b in boxes.splitlines(): ## List Include Separated Lines
    b = b.split(" ") ## Split Each Eelement Of The Line
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[2]), int(b[4])
    cv2.rectangle(img, (x,img_h-y), (w, img_h-h), (0,255,0), 1)
    cv2.putText(img, b[0], (x,img_h-y+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 2)
    

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()