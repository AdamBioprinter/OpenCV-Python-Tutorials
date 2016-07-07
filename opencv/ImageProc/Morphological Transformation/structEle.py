# In the morphological operations files in this folder, we created a structuring with the help of numpy (a rectangular structuring element)

# sometimes we may need different shape kernels

# OpenCV has a function just for that:

# cv2.getStructuringElement()

import cv2
import numpy as np

Ker1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
ker2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
Ker3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

print('rectangular kernel: ', Ker1)
print('elliptical kernel: ', ker2)
print('cross shaped kernel: ', Ker3)

