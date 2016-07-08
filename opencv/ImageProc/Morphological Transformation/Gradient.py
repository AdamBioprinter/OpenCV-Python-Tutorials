# In this script there are three types of gradient filters or High-pass filters used: sobel, scharr, laplacian

# sobel: joint gaussian smoothing and differentiation - more resistant to noise

# if ksize of -1 is specified, a 3x3 scharr filter used

# laplacian: calculates laplacian of image
# LapSrc = d^2(src)/dx^2 + d^2(src)/dy^2
# if ksize = 1, the following kernel is used:
# kernel = [0 1 0; 1 -4 1; 0 1 0]

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('PaperIM.JPG',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

plt.subplot(221), plt.imshow(img,'gray'), plt.title('Original')
plt.axis('off')
plt.subplot(222), plt.imshow(laplacian,'gray'), plt.title('Laplacian')
plt.axis('off')
plt.subplot(223), plt.imshow(sobelx,'gray'), plt.title('Sobel X')
plt.axis('off')
plt.subplot(224), plt.imshow(sobely,'gray'), plt.title('Sobel Y')
plt.axis('off')
plt.show()

