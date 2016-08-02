# 4 point OpenCV getPerspectiveTransform Example

import numpy as np
import cv2

# it is important to note that this function assumes the points are in (x ,y) coordinate 
# format. As opposed to traditional (row, col).
# The coordinate format is typically returned from the findContour function, 
# so the conversion isn't apparent in the script
def order_points(pts):

  # initialize a list of coordinates that will be ordered such that 
  # the first entry in the list is the top-left, the second entry is
  # the top right, the third is the bottom right, and the fourth is the
  # bottom left
  rect = np.zeros((4,2), dtype = "float32")

  # the top left point will have the smallest sum, whereas 
  # the bottom right right will have the largest sum
  s = pts.sum(axis = 1) # axis 1 specifies to sum elements along the horizontal direction
  rect[0] = pts[np.argmin(s)]
  rect[2] = pts[np.argmax(s)]

  # now, compute the difference between the points, the top-right point 
  # will have the smalles difference, whereas bottom left will have 
  # the largest differene

  # the diff command, about axis 1, subtracts the first column from the second column.
  # Hence, (x,y) coordinates fit with this format
  diff = np.diff(pts, axis = 1)
  rect[1] = pts[np.argmin(diff)]
  rect[3] = pts[np.argmax(diff)]

  # return the ordered coordinates
  return rect

def four_point_transform(image,pts):

  # obtain a consistent order of points and unpack them individually
  rect = order_points(pts)
  (tl, tr, br, bl) = rect

  # compute the width of the new image, which will be the 
  # maximum distance between bottom right and bottom left x-coordinates 
  # or top right and top left x coordinate
  widthA = np.sqrt(((br[0] - bl[0])**2) + ((br[1]-bl[1])**2))
  widthB = np.sqrt(((tr[0] - tl[0])**2) + ((tr[1]-tl[1])**2))
  maxWidth = max(int(widthA), int(widthB))

  # compute height of new image
  heightA = np.sqrt(((tr[0] - br[0])**2) + (( tr[1] - br[1])**2))
  heightB = np.sqrt(((tl[0] - bl[0])**2) + (( tl[1] - bl[1])**2))
  maxHeight = max(int(heightA), int(heightB))

  # construct set of destination points to obtain a "birds eye view"
  # it is important to note that the dst is structured appropriately to rect,
  # as (tl, tr, br, bl). Recall the cv2.getPerspectiveTransform() takes x,y coordinates.
  # not row, column
  dst = np.array([
    [0,0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype = "float32")

  # compute perspective transform matrix and the apply
  # recall that cv2.warpPerspective takes a 3x3 transformation matrix 
  # and this matrix can be computed with cv2.getPerspectiveTransform(image, M, (dst size))
  M = cv2.getPerspectiveTransform(rect, dst)
  warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
  
  #return the warped image
  return warped

def resize(image, height=1000.0):
  
  # this function is just an easy way to resize an image while 
  # keeping the same aspect ratio
  r = height/image.shape[1]
  dim = (int(height), int(image.shape[0] *r))

  # recall cv2.resize takes (x,y), as in (width, height)
  # which is flipped from the matrix subscript notation:
  # (row, column)
  resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

  return resized 


