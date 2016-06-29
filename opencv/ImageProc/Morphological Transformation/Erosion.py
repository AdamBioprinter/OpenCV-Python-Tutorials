# Erosion erodes away the boundary of a foreground object (always try to keep foreground white)
# The kernel slides through the image (as in 2D convolution)
# a Pixel in the original image (usually binary) will be considered 1 iff all pixels under the kernel are 1

# useful in removing small white noise

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

plt.subplot(121), plt.imshow(img,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Original Image')
plt.subplot(122), plt.imshow(erosion,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Eroded image')
plt.show()
