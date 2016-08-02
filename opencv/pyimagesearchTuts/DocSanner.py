import cv2
import transform
import numpy as np
import argparse
from skimage.filters import threshold_adaptive

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image to be scanned")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print('Original image shape: ',image.shape)
ratio = image.shape[1]/300.0
orig = image.copy()
image = transform.resize(image, height = 300.0)
print('image shape: ', image.shape)
# conver the image to grayscale, blur it, and find edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected image
print('STEP 1: Edge Detection')
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find the countours in the edges image, keeping only the largest ones,
# and initialize hte screen contour
(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

# debbuger
# print('cnt[0]: ', cnts[0])
# print('cnt[1]: ', cnts[1])
# loop over contours
for c in cnts:
  # approximate contour as polygon
  eps = 0.08*cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, eps, True)

  # if out approximated contour has four points, then we can assume that 
  # we have found our screen
  if len(approx) == 4:
    screenCnt = approx
    break

print('screenCnt: ', screenCnt)
print('screenCnt.shape: ', screenCnt.shape)
# show the contour (outline) of the piece of paper
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0,255,0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# screenCnts are given in x,y coordinates
# we are going to convert them flip it to (y,x), or traditional matrix subscript for the four point transform

# screenCnt2 = np.zeros((4,2), dtype='uint16')
# screenCnt2[:,0] = screenCnt.reshape(4,2)[:,1]
# screenCnt2[:,1] = screenCnt.reshape(4,2)[:,0]
# print('screenCnt2: ', screenCnt2)
# print('screenCnt2*ratio: ',screenCnt2*ratio)
# print('screenCnt2.shape: ', screenCnt2.shape)

# applt the four point transform to obtain a top-down
# view of the original image
warped = transform.four_point_transform(orig, screenCnt.reshape(4,2)*ratio)

print('first warp command')
print('warp shape: ',warped.shape)
print('warped dtype: ', warped.dtype)
cv2.imshow("warped",transform.resize(warped, height = 300.0))
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the warped image to grayscale, then 
# threshold it to give it that "black and white"
# paper effect
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warped = threshold_adaptive(warped, 51, offset=10) # returns logical matrix
print('post thresh warped shape: ', warped.shape)
print('max intensity: ', warped.max())
warped = warped.astype("uint8")*255 # convert to 8-bit

# show the original and scanned images
print('STEP 3: Apply perspective transform')
cv2.imshow("Original", transform.resize(orig, height=300.0))
cv2.imshow("Scanned", transform.resize(warped, height=300.0))
cv2.waitKey(0)
cv2.destroyAllWindows()

