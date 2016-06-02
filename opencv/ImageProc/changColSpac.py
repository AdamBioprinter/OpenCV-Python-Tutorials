import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
# print('lower_blue: ' + str(lower_blue))
upper_blue = np.array([130,255,255])
# print('upper_blue: ' + str(upper_blue))

while(cap.isOpened()):

  #take each frame
  ret, frame = cap.read()

  #convert BGR to HSV
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv, lower_blue, upper_blue)

  # bitwise-AND mask and original image
  res = cv2.bitwise_and(frame,frame, mask=mask)

  # resize each image to be half the width and height, display each frame
  frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
  cv2.imshow('frame',frame)

  mask = cv2.resize(mask,(0,0),fx=0.5, fy=0.5)
  cv2.imshow('mask',mask)

  res = cv2.resize(res,(0,0), fx=0.5, fy=0.5)
  cv2.imshow('res',res)

  # resize the windows
  #  cv2.resize('res',(80,45))

  k = cv2.waitKey(5) & 0xFF

  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()


