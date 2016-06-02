# Otsu's Binarization
# Used for bimodal images!!!!!!!!!!!
# automatically calculates a thershold value from image histogram for bimodal image - return threshold in retVal
# This threshold method will not be accurate for images that are not bimodal

import cv2
import numpy as np
from matplotlib import pyplot as plt

# recall 0 in the second argument reads the image as a grayscale
img = cv2.imread("grey square.png",0)

# global thresholding
ret1, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding - pass an extra flag: cv2.THRESH_OTSU
# pass 0 for threshold value
ret2, th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thesholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plotting all images with their histograms
images = [img,0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',\
    'Original Noisy Image','Histogram',"Otsu's Thesholding", \
    'Gaussain filtered image','Histogram',"Otsu's Thresholding"]

for i in range(3):
  plt.subplot(3,3,i*3+1), plt.imshow(images[i*3],'gray')
  plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
  plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
  plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
  plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
  plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
