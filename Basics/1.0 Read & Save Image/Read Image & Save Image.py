"""
Created on Sun Aug 22 01:04:54 2021
@author: Eriny
"""

import cv2

img = cv2.imread('./apple.jpg', 1) ## 0 -> GrayScale, 1 -> RGB, -1 -> Alpha Channel
cv2.imshow("Apple", img)
## Print Pixels Of The Image
print(img)

cv2.waitKey(5000) ## Using Any Num Except 0/1 --> Waits for # millisecond
cv2.destroyAllWindows()

## OR
"""
pressedKey = cv2.waitKey(0) ## Using 0 --> Waits a key from user & X Sign close it also, Using 1 --> Waits a key from user & X Sign does not close
if pressedKey == 27:        ## 27 == Esc button in keyboard
    cv2.destroyAllWindows()
elif pressedKey == ord('s'):
    cv2.imwrite("Saved Apple.jpg", img) ## Save image in the same directory
    cv2.destroyAllWindows()
else:
    pass
"""