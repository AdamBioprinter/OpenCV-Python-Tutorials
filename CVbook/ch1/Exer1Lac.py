import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.ndimage import filters

im = np.array(Image.open('Image 4_z34.tif'))

# The second argument defines the standard deviation in the gaussian kernel
im2 = filters.gaussian_filter(im,5)
im3 = filters.gaussian_filter(im,10)
im4 = filters.gaussian_filter(im,15)
im5 = filters.gaussian_filter(im,20)

plt.gray()
plt.subplot(251), plt.imshow(im),plt.title('Original Image')
plt.axis('equal'), plt.axis('off')
plt.subplot(256), plt.contour(im, origin='image'), plt.axis('equal')
plt.axis('off')

plt.subplot(252), plt.imshow(im2),plt.title(r'$\sigma$ = 5')
plt.axis('equal'), plt.axis('off')
plt.subplot(257), plt.contour(im2, origin='image'), plt.axis('equal')
plt.axis('off')

plt.subplot(253), plt.imshow(im3),plt.title(r'$\sigma$ = 10')
plt.axis('equal'), plt.axis('off')
plt.subplot(258), plt.contour(im3, origin='image'), plt.axis('equal')
plt.axis('off')

plt.subplot(254), plt.imshow(im4),plt.title(r'$\sigma$ = 15')
plt.axis('equal'), plt.axis('off')
plt.subplot(259), plt.contour(im4, origin='image'), plt.axis('equal')
plt.axis('off')

plt.subplot(255), plt.imshow(im5),plt.title(r'$\sigma$ = 20')
plt.axis('equal'), plt.axis('off')
plt.subplot(2,5,10), plt.contour(im5, origin='image'), plt.axis('equal')
plt.axis('off')
plt.show()
