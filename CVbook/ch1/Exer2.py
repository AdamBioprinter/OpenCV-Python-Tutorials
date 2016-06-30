import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.ndimage import filters

im = np.array(Image.open('building.jpg').convert('L'))

# The second argument defines the standard deviation in the gaussian kernel
im2 = filters.gaussian_filter(im,5)
im3 = filters.gaussian_filter(im,10)

outIM1 = im-im2*0.5
outIM2 = im-im3*0.5
plt.gray()
plt.subplot(131), plt.imshow(im), plt.title('Original Image')
plt.axis('equal'), plt.axis('off')
plt.subplot(132), plt.imshow(outIM1), plt.title('Unsharped with 'r'$\sigma$=5')
plt.axis('equal'), plt.axis('off')
plt.subplot(133), plt.imshow(outIM2), plt.title('Unsharped with 'r'$\sigma$=10')
plt.axis('equal'), plt.axis('off')
plt.show()
