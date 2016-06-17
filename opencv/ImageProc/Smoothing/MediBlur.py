import cv2
import numpy as np
from matplotlib import pyplot as plt

# Median blur is particularly effective on salt and pepper noise
img = cv2.imread('openCV_logo.png')

# Adding noise to image, specifically salt and pepper
# STUCK HERE!!!!!!!!!!

blur = cv2.medianBlur(img2,5)

blur2 = cv2.medianBlur(img2,21)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img2),plt.title('Noised Image')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur),plt.title('Blurred 5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur2),plt.title('Blurred 21')
plt.xticks([]), plt.yticks([])
plt.show()
