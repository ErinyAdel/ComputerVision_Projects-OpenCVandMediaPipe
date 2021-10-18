# -*- coding: utf-8 -*-

"""
Created on Mon Oct 18 12:50:00 2021
@author: Eriny
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
img_h, img_w, _ = img.shape

config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, lang="eng", config=config)
print(boxes)
for b in boxes.splitlines():
    b = b.split(" ") ## Split Each Value For The Separated Line, By Comma (In List)
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,img_h-y), (w,img_h-h), (100,144,0), 2)
    cv2.putText(img, b[0], (x,img_h-y+15), 2, 0.5, (100,100,0), 1)
            
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()