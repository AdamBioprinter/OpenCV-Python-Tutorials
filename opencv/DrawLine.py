import numpy as np
import cv2
from matplotlib import pyplot as plt

# create a black image
img = np.zeros((512,512,3), np.int8)

# Draw a diagonal blue line with thickness of 5 pixels
# input arguments for cv2.line():
# cv2.line(image, start, end, color, thickness)
# recall opencv sees images as BGR (NOT RGB)
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle
# input arguments:
# cv2.rectangle(image,top left corner, bottom right corner, color, thickness)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),2)

# drawing a circle
# input arguments
# cv2.circle(image,center, radius, color, thickness
# recall if thickness is -1, the shape is filled
# centerx = 384+(510-384)/2
cv2.circle(img,(447,60),63,(0,0,255),-1)

# drawing an elipse
# input argument
# cv2.ellipse(image,center,axes length (major axis length, minor axis length),angle, start angle, end angle, color, thickness
# recall if color is a scalar, the input is in grayscale
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# drawing a polygon
# input arguments:
# First you need coordinates of vertices, should be type int32
# make the points into an array of shape (Row,1,2), where rows are the number of vertices
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# adding text
# input coordinates:
# cv2.putText(image, text, position coordinate, font type, font scale, color, thickness
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

# cv2.imshow('image',img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows
