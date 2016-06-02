import cv2
import numpy as np
from matplotlib import pyplot as plt

# image addition with numpy works differently then cv2
x = np.uint8([250])
y = np.uint8([10])

# opencv addition is saturated, while numpy addition is a modulo operation
print("cv2 addition: " + str(cv2.add(x,y)))
print("numpy addition: " + str(x+y))

# Image Blending
# weighted average - arrays must be of same size

img1 = cv2.imread('apple.jpg')
img2 = cv2.imread('Bioprinter_Circuit_Lg_bb copy.png')

img1S = list(img1.shape)
img2S = list(img2.shape)

# crop image2 to be of same size as img1
img1Mod = img1[0:img2S[0],0:img2S[1]]
print("img1 Size: " + str(img1S))
print("img2 Size: " + str(img2S))
print("New img1: " + str(img1Mod.shape))

# now that we have 2 images of the same size ...
dst = cv2.addWeighted(img1Mod,0.65,img2,0.35,0)

# rearrange channels to rgb for matplotlib graphing
[b, g, r] = cv2.split(dst)
dst2 = cv2.merge([r,g,b])

plt.imshow(dst2, cmap = 'jet', interpolation = 'bicubic')
plt.title("Image Blending")
plt.xticks([]), plt.yticks([])
plt.show()

# cv2.destroyAllWindows()

