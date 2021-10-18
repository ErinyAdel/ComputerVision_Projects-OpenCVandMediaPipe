"""
Created on Sun Aug 22 22:48:19 2021
@author: Eriny
"""

import cv2

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)
font = cv2.FONT_HERSHEY_SIMPLEX

## --------------------------------------------------------------------------

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: ## Left Button
        strXY = str(x) + ', '+ str(y)  ## Get The Coordinates
        cv2.putText(img, strXY, (x,y), font, .3, (0, 0, 0), 1)
        cv2.imshow('Image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN: ## Right Button
        ## Get The RGB Values    
        blue  = img[y,x,0]
        green = img[y,x,1]
        red   = img[y,x,2]
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x,y), font, .3, (255, 255, 255), 1)
        cv2.imshow('Image', img)
        
## --------------------------------------------------------------------------

img = cv2.imread('apple.jpg')
cv2.imshow('Image',img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()