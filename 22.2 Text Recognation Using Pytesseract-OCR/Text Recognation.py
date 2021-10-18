# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:38:21 2021
@author: Eriny
"""

"""
Fonts:
    
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('test.png')
img_h, img_w, _ = img.shape

boxes = pytesseract.image_to_data(img)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0: ## Skip 'Level' Column (Index 0)
        b = b.split() ## Split Each Value For The Separated Line, By Comma (In List)
        print(b)
        if len(b) == 12: ## Take The Values Which Include Values For 'Text' Column
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (x+w,y+h), (100,144,0), 2)
            cv2.putText(img, b[11], (x,y), 2, 0.8, (100,100,0), 1)
            
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()