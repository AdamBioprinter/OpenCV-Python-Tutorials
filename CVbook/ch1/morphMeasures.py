import numpy as np
from scipy.ndimage import measurements, morphology
from PIL import Image
import cv2
from matplotlib import pyplot as plt

# load image
im = cv2.imread('Binary Objects.jpg',0)

# thresholding
ret, thresh1 = cv2.threshold(im,127,255,cv2.THRESH_BINARY)

thresh1 = np.array(thresh1,'uint8')

labels, nbr_objects = measurements.label(thresh1)

print('Number of objects prior to closing: ',nbr_objects)
plt.figure(1)
plt.subplot(131), plt.imshow(im,'gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(132), plt.imshow(thresh1,'gray'), plt.title('Binarized image'), plt.axis('off')
plt.subplot(133), plt.imshow(labels,'gray'), plt.title('Indexed Image'), plt.axis('off')

# morphology - closing to better represent objects
im_close = morphology.binary_closing(thresh1,np.ones((3,3)), iterations=2)
# the second argument specifies the structuring element, an array 
# that indicates what neighnots to use when centered around a pixel
labels, nbr_objects = measurements.label(im_close)
print('Number of objects after to closing: ',nbr_objects)
plt.figure(2)
plt.subplot(121), plt.imshow(im,'gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(122), plt.imshow(im_close,'gray'), plt.title('closed image'), plt.axis('off')

plt.show()
