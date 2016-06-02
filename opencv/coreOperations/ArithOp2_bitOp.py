import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading the images
MesImg = cv2.imread('Lionel-Messi.jpg')
OCVImg = cv2.imread('OpenCV_Logo2.png')

print("Messi Size: " + str(MesImg.shape))


# We want to put the logo on the top-left corner, so create an ROI
rows, cols, channels = OCVImg.shape
roi = MesImg[0:rows, 0:cols]

#convert logo to grayscale
img2gray = cv2.cvtColor(OCVImg,cv2.COLOR_BGR2GRAY)

#[b, g, r] = cv2.split(img2gray)
#img2grayMPL = cv2.merge([r,g,b])

# plt.imshow(img2gray, cmap='gray')
# plt.xticks([]), plt.yticks([])
# plt.show()

# cv2.imshow('GrayLog',img2gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# use threshold to creat a mask
ret, mask = cv2.threshold(img2gray, 151, 255, cv2.THRESH_BINARY)

# print("ret: " + str(ret))

cv2.imshow('ThreshLogo',mask)
cv2.waitKey(0)
cv2.destroyAllWindows

# calculate inverse of mask
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('InverseMask',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows

# now black-out the area of logo in ROI
MesImg_bg = cv2.bitwise_and(roi,roi,mask = mask)

cv2.imshow('MesImg',MesImg_bg)
cv2.waitKey(0)
cv2.destroyAllWindows

# Taking only the region of the logo from the logo image

OCVImg_fg = cv2.bitwise_and(OCVImg, OCVImg, mask = mask_inv)

#put logo in ROI and modify the main image
dst = cv2.add(MesImg_bg,OCVImg_fg)
MesImg[0:rows, 0:cols] = dst

cv2.imshow('res',MesImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

