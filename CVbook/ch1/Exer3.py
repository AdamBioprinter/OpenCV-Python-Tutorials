# this exercise an histogram equalization using a quotient image.
# this is obtained by dividing the image with a blurred version

from PIL import Image
import numpy as np
from scipy.ndimage import filters
from matplotlib import pyplot as plt

im = np.array(Image.open('building.jpg').convert('L'))

# The second argument defines the standard deviation in the gaussian kernel
im2 = filters.gaussian_filter(im,10)
im3 = filters.gaussian_filter(im,20)

HistEqIM = im/im2
HistEqIM2 = im/im3

plt.gray()
plt.subplot(131), plt.imshow(im),plt.title('Original Image')
plt.axis('off')
plt.subplot(132), plt.imshow(HistEqIM) ,plt.title('std = 10 Blur')
plt.axis('off')
plt.subplot(133), plt.imshow(HistEqIM2),plt.title('std = 20 Blur')
plt.axis('off')
plt.show()
