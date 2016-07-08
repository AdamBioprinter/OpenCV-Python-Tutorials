# cv2.canny() --> edge detector
# first step - noise reduction
#   -the algorithm utlizes a 5x5 Gaussian filter
# second step - Intensity Gradient of image
#   -image is filtered with a sobel kernel in both directions (x and y) to 
#   find first derivative
#   -This step determines the "norm" edge gradient sqrt(Gx^2+Gy^2)
#   - and the angle theta = atan(Gy/Gx)
#   the angle is rounded to one of four angles (horizontal, vertical, and 
#   two diagonal
# thrid step - filter pixels
#   all pixels are checked if its a local maximum in the direction of gradient
# fourth step - thresholding filter
#   - two threshold are used: minVal, maxVal
# if edge intensity gradient > maxVal its an edge
# if edge intensity gradient < minVal discard
# if minVal < edge instensity gradient < maxVal, classified based on connectivity

#syntax: cv2.canny(img,minVal,maxVal, option: aperature_size, L2gradient)
# aperature size specifies the sobel kernel used to find image gradient
# default is 3x3
# L2gradient specifies equation for finding gradient magnitude. 
# True uses norm equation, Flase uses abs(Gx)+abs(Gy)
# default is False

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('LacIM.tif',0)

edges = cv2.Canny(img,150,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
