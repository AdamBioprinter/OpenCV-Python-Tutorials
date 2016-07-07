# a morpholgical gradient is the difference between a dilation and erosion of an image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0) # consider adding random gaussian noise
kernel = np.ones((5,5),np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121), plt.imshow(img,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Original Image')
plt.subplot(122), plt.imshow(gradient,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Gradient image')
plt.show()
