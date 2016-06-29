# Dilation dilates the boundary of a foreground object (always try to keep foreground white)
# The kernel slides through the image (as in 2D convolution)
# a Pixel in the original image (usually binary) will be considered 1 if at least 1 pixel under the kernel is 1

# dilation is usually preceded by an erosion
# the erosion is used to remove noise, and dilation is used to bring objects back to original area/volume

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Original Image')
plt.subplot(122), plt.imshow(dilation,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Dilated image')
plt.show()
