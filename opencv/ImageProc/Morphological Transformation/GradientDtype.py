# in openCV, black to white transition is taken as positive slope
# therfore, white to black transition is taken to be negative slope.

# if you convert data to np.uint8, all negative slopes are made 0
# so you miss that an edge marked by white to black transition (depends on rastering scheme of kernel)

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imsave

# img = np.zeros((1000,800))
# img[300:700,200:600] = 1

# imsave('box.jpg',img)
img = cv2.imread('box.jpg',0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()
