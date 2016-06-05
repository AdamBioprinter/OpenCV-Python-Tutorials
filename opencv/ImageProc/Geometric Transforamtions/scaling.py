# scaling is just resizing an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('PaperIM.JPG')

res1 = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)

# OR

height, width = img.shape[:2]

# It is important to note this method must accept integer, as it literally takes the number of pizels along the height and width

res2 = cv2.resize(img,(int(width*0.3), int(height*0.3)), interpolation = cv2.INTER_CUBIC)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)

cv2.waitKey(0) & 0xFF # this command waits for user the press esc, and then continues execution
cv2.destroyAllWindows()

