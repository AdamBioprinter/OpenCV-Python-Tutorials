from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# read in image as array
im = np.array(Image.open('building.jpg').convert('L'))

# create figure
plt.subplot(121)

# No colors
plt.gray()

# show contours with origin upper left corner
plt.contour(im,origin='image')
plt.axis('equal')
plt.axis('off')

# histogram - create separate figure
plt.subplot(122)

# hist takes a one dimesnional array input
# the flatten() method converts any array to 1D array with values taken row-wise
plt.hist(im.flatten(),128)

plt.show()
