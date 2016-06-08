#rotation of image by angle theta is achieved with transformation matrix:
# M = [[cos(th) -sin(th)],[sin(th) cos(th)]]

# OpenCV provides scaled rotation with adjustable center of rotation.
# This modified tranformation matrix is given by:
# M = [[Alpha, Beta, (1-Alpha)*center.x-Beta*center.y], \
    #  [-Beta, Alpha, Beta*center.x+(1-Alpha)*center.y]]

# where Alpha = scale*cos(th)
# and Beta = scale*sin(th)

# Luckily, OpenCV provides a fundtion that will determine this rortation matrix:
# M = cv2.getRotationMatrix2D(center, rotation, scale)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('PaperIM.JPG',0) # recall the passing 0 as the second argument reads the image as a grayscale

# resize image (so it fits on my screen)
# img = cv2.resize(img,None, fx=0.2, fy = 0.2)

rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
outIMG = cv2.warpAffine(img,M,(cols, rows))

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(outIMG, cmap='gray')
plt.title('Rotated Image')
plt.xticks([]), plt.yticks([])
plt.show()
# cv2.imshow('Original Image',img)
# cv2.imshow('Rotated Image',outIMG)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
