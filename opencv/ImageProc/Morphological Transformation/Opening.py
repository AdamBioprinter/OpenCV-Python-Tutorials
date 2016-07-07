# dilation is usually preceded by an erosion
# the erosion is used to remove noise, and dilation is used to bring objects back to original area/volume
# this combination of erosing followed by dilation is called opening

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png',0) # consider adding random gaussian noise
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121), plt.imshow(img,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Original Image')
plt.subplot(122), plt.imshow(opening,'gray'), plt.axis('equal'), plt.axis('off')
plt.title('Opened image')
plt.show()
