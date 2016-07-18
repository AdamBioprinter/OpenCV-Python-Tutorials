# contours are curves joining all continous points having the same color 
# or intesnity

# it is recommended to use binary images - apply threshold beforehand
# the findCoontours function DOES modify the source image
# the function finds white objects in a black background

# syntax:
# cv2.findCountrous(src, contour retrieval mode, contour approximation 
# method)

# 3 output arguments!

#use: image, contours, hierarchy = cv2.findCountours(thresh, cv2.RETR_TREE, cv2.CHAIN_AAPPROX_SIMPLE)

# in order to draw contours, use cv2.drawContours function
# img = cv2.drawContours(img, contours, contour indx (-1 for all), color, thickness)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Convex_shape.jpg') # read image 
print('data type of img: ',img.dtype)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY) # make image binary
ret2, thresh2 = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
img2, contours, hierarchy  =cv2.findContours(thresh2, cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

# print(M)

# centroid

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('Center coordinate: (',cx, ', ', cy, ')')

# area

area = cv2.contourArea(cnt)
area2 = (M['m00'])

print('area: ', area)
print('area measured with moments: ', area2)

# perimeter
# second argument specifies if shape is a closed contour

perimeter = cv2.arcLength(cnt, True)

print('Perimter length: ',perimeter)

# contour approximation
eps1 = 0.1*cv2.arcLength(cnt, True)
eps2 = 0.01*cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt,eps1, True)
approx2 = cv2.approxPolyDP(cnt,eps2, True)

print('approx1: ', approx1)
print('approx2: ', approx2)

# draw contours on image
ContouredIM = cv2.drawContours(thresh.copy(), approx1, -1, (0,255,0),3)

# plot contour approximation
plt.figure(1)
plt.subplot(131), plt.imshow(thresh, 'gray'), plt.title('Original Image (binary)')
plt.axis('off')
plt.subplot(132), plt.imshow(ContouredIM), plt.title('Approximated contours')
plt.axis('off')
plt.show()
