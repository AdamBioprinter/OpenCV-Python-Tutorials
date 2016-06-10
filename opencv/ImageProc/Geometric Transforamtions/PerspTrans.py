# Perspective Transformation

# Stuff you need:

# - 4 points on input image
# - 4 points on output image (corresponding)
# - 3 of them shall be collinear
# - a 3x3 transformation matrix - found with cv2.getPerspectiveTransform

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("PaperIM.JPG")
rows,cols,ch = img.shape

pts1 = np.float32([[256, 365],[2000, 350],[337, 1996],[2002,3000]])
pts2 = np.float32([[0,0],[1500,0],[0,1500],[1500,1500]])

M = cv2.getPerspectiveTransform(pts1,pts2)

outIM = cv2.warpPerspective(img,M,(1500,1500))

plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Input')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(outIM, cmap='gray'),plt.title('Output')
plt.xticks([]), plt.yticks([])
plt.show()


