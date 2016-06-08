# In Affine transformation, all parallel lines in the original image will still be parallel in the output image.

# we need three points from the input image and their corresponding locations in the output image.

# cv2.getAffineTransform() will creat a 2x3 matrix that can be passed to 
# cv2.warpAffine()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Chess Board.jpg')
rows, cols, ch = img.shape

# It seems like the points are stored in (y,x) aka (cols,rows)
# strange!
pts1 = np.float32([[100,100],[270,100],[100,270]])
pts2 = np.float32([[10,180],[270,100],[180,370]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
