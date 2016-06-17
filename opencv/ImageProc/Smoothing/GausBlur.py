import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('openCV_logo.png')

# In gaussian filtering, the standard deviation need to be specify the x and y
# Standard deviations
# If only one is given, then it assumes the same for the other
# if both are given as zeros, they are calculated from the kernel size
# width and height of gaussian kernel must be positive and odd
blur = cv2.GaussianBlur(img,(5,5),0)

blur2 = cv2.GaussianBlur(img,(21,21),0)

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred 5x5')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Blurred 20x20')
plt.xticks([]), plt.yticks([])
plt.show()
