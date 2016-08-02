import numpy as np
import argparse
import glob
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

# load image
imagePath = 'j.png'
image = cv2.imread(imagePath,0)

# blurred = cv2.GaussianBlur(gray,(3,3),0)

auto = auto_canny(image)
auto2 = auto_canny(image, sigma=0.4)
auto3 = auto_canny(image, sigma=0.25)

plt.subplot(221), plt.imshow(image,'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(222), plt.imshow(auto,'gray'), plt.title('automatic edge detector')
plt.axis('off')
plt.subplot(223), plt.imshow(auto2,'gray'), plt.title('auto2 - sigma=0.4')
plt.axis('off')
plt.subplot(224), plt.imshow(auto3,'gray'), plt.title('auto3 - sigma=0.25')
plt.axis('off')
plt.show()





