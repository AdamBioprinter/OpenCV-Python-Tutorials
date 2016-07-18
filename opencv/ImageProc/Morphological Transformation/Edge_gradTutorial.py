import cv2
import numpy as np

def auto_canny(image, sigma=0.33):

  # compute the median of the single channel pixel intensities
  v = np.median(image)

  # determine minVal and MaxVal as a percentage difference from the median
  lower = int(max(0,(1.0-sigma)*v))
  upper = int(max(0,(1.0+sigma)*v))
  
  # apply automatic edge detection
  edged = cv2.Canny(image,lower,upper)

  return edged 

cap = cv2.VideoCapture(0)

cv2.namedWindow("Original",cv2.WINDOW_NORMAL)
# cv2.namedWindow("laplacian",cv2.WINDOW_NORMAL)
cv2.namedWindow("edges",cv2.WINDOW_NORMAL)
# cv2.namedWindow("sobelx",cv2.WINDOW_NORMAL)
# cv2.namedWindow("sobely",cv2.WINDOW_NORMAL)
cv2.namedWindow("edges2",cv2.WINDOW_NORMAL)

while True:
  _, frame = cap.read()

  # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
  # sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
  # sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
  edges = cv2.Canny(frame,100,200)
  edges2 = auto_canny(frame)

  cv2.imshow('Original', frame)
  # cv2.imshow('laplacian',laplacian)
  # cv2.imshow('sobelx', sobelx)
  # cv2.imshow('sobely',sobely)
  cv2.imshow('edges',edges)
  cv2.imshow('edges2',edges2)

  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()
cap.release()
