import cv2
import numpy as np
from matplotlib import pyplot as plt

# read in image in grayscale
img = cv2.imread('PaperIM.JPG',0)
print("Image type: " + str(img.dtype))
# resize image to fit screen (used when using cv2.imshow) 
# img = cv2.resize(img,(0,0),fx=0.2, fy=0.2)

# display image
# cv2.imshow('original',img)

# perform a median blur on the image
img = cv2.medianBlur(img,5)

# display processed image
# cv2.imshow('Processed',img)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# syntax for adaptive thresholding: 
# output = cv2.adaptiveThreshold(image,maxValue, adaptive method, threshold type, blocksize, C)

# maxValue - non-zero value assigned to the pizels for which the condition is satisfied

# C - constant subtracted from the mean or weighted mean

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v=127)',\
    'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
  plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]), plt.yticks([])

plt.show()
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

