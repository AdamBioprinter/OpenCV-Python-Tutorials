import cv2
import numpy as np
from matplotlib import pyplot as plt

# load a color image. Uses the command cv2.imread(filepath,flag)
# flag = 1 loads a color image (transparency will be negleted)
# flag = 0 loads image in grayscale
# flag = -1 loads image as such including alpha channel
# filepath can be ommited if image is in working directory, in which case file name still needs to be included
# Ex: "ExammpleIM.jpg"

img = cv2.imread('Collapsed Image.png',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
if k == 27: # wait for ESC key to exit
  cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
  cv2.imwrite('Yomama.png',img)
  cv2.destroyAllWindows() 
