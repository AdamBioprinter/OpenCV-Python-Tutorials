import cv2
import numpy as np,sys

A = cv2.imread('apple3.jpg')
B = cv2.imread('orange.jpg')

# generate gaussian pyramid for A
G = A.copy()
gpA = [G] # start building gaussian pyramid in a list
for i in range(6):
  G = cv2.pyrDown(gpA[i])
  gpA.append(G)

# generate Gausian pyramid for B
G = B.copy()
gpB = [G] # start building gaussian pyramid in a list
for i in range(6):
  G = cv2.pyrDown(gpB[i])
  gpB.append(G)

# generate laplacian pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
  size = (gpA[i-1].shape[1], gpA[i-1].shape[0])
  GE = cv2.pyrUp(gpA[i], dstsize=size)
  L = cv2.subtract(gpA[i-1],GE)
  lpA.append(L)

# generate laplacian pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
  size = (gpB[i-1].shape[1], gpB[i-1].shape[0])
  GE = cv2.pyrUp(gpB[i],dstsize = size)
  L = cv2.subtract(gpB[i-1],GE)
  lpB.append(L)

# now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
  rows,cols,dpt = la.shape
  ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
  LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
  size = (LS[i].shape[1], LS[i].shape[0])
  ls_ = cv2.pyrUp(ls_, dstsize = size)
  ls_ = cv2.add(ls_,LS[i])
  
# image with direct connecting rach half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
