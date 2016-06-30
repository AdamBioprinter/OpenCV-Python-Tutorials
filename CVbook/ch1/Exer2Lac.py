import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.ndimage import filters

im = np.array(Image.open('Image 4_z34.tif'))

# The second argument defines the standard deviation in the gaussian kernel
im2 = filters.gaussian_filter(im,10)
im3 = filters.gaussian_filter(im,20)

outIM1 = im-im2*0.5
outIM2 = im-im3*0.5
plt.gray()
plt.subplot(131), plt.imshow(im), plt.title('Original Image')
plt.axis('equal'), plt.axis('off')
plt.subplot(132), plt.imshow(outIM1), plt.title('Unsharped with 'r'$\sigma$=10')
plt.axis('equal'), plt.axis('off')
plt.subplot(133), plt.imshow(outIM2), plt.title('Unsharped with 'r'$\sigma$=20')
plt.axis('equal'), plt.axis('off')
plt.show()
