# this is similar to the start contour code
# the purpose of this script is to identify the outer contours of a hand, from an image taken with a camera phone

import numpy as np
import cv2
from matplotlib import pyplot as plt

def auto_canny(image, sigma=0.33):

  # compute the median of the single channel pixel intensities
  v = np.median(image)

  # determine minVal and MaxVal as a percentage difference from the median
  lower = int(max(0,(1.0-sigma)*v))
  upper = int(max(0,(1.0+sigma)*v))
  
  # apply automatic edge detection
  edged = cv2.Canny(image,lower,upper)

  return edged 

img = cv2.imread('handIM3.jpg')
B,G,R = cv2.split(img)
RGBimg = cv2.merge((R,G,B))

# print('img [dtype shape]: [',img.dtype, img.shape,']')
# convert to grayscale
GrayIM = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print('GrayIM [dtype shape]: [',GrayIM.dtype, GrayIM.shape,']')
# smooth
SmooIM = cv2.bilateralFilter(GrayIM, 21, 47, 47)

# take the inverse of the image (so the foreground is white and background black)
invSmoo = cv2.bitwise_not(SmooIM)

# apply additional gaussian filter
MedFilt = cv2.medianBlur(invSmoo, 55)
MedFilt2 = cv2.medianBlur(MedFilt, 35)

# edge detection
Edged = cv2.Canny(invSmoo, 0, 10)
Edged_aut = auto_canny(invSmoo, sigma=0.05)

# laplacians
# Lap1 = cv2.Laplacian(invSmoo, cv2.CV_64F)
plt.subplot(131), plt.imshow(invSmoo, cmap = 'gray'), plt.title('Smoothed Image')
plt.axis('off')
plt.subplot(132), plt.imshow(Edged, 'gray'), plt.title('Edged')
plt.axis('off')
plt.subplot(133), plt.imshow(Edged_aut, 'gray'), plt.title('Auto Edged')
plt.axis('off')
plt.show()



