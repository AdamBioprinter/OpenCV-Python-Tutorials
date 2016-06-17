import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('openCV_logo.png')

blur = cv2.blur(img,(5,5))

blur2 = cv2.blur(img,(20,20))

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur),plt.title('Blurred 5x5')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Blurred 20x20')
plt.xticks([]), plt.yticks([])
plt.show()
