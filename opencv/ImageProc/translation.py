#translation is shifting of object's location
# say the shift is known in (x,y), create transformation matrix M:
# M = [1 0 x; 0 1 y], make it into numpy array of type np.float32 and pass to cv2.wartAffine()
#example for a shift of (100,50)

import cv2
import numpy as np

img = cv2.imread('PaperIM.JPG',0)
rows, cols = img.shape

M = np.float32([[1,0,100],[0, 1,50]])

# outputIM = cv2.warpAffine(image, M, (width, height))
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0) # this command waits until user presses anything
cv2.destroyAllWindows()
