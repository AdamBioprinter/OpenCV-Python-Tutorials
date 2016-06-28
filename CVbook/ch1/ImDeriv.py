# Image derivatives describe how the image intensity changes over the image
# the change is described with the x and y derivatives (Ix and Iy) for a 2D graylevel image.
# for color images, the derivatives are usually evaluated for each color channel
# Image Gradient is a vector = [Ix, Iy]'

# gradient magnitude = sqrt(Ix**2 + Iy**2)
# describes how strong the image intensity change is

# gradient angle = np.arctan2(Iy, Ix)
# direction of largest intesity change 

# computing derivatives is usually done with discrete approximations with convolutions
# see sobel and prewitt filters in the scipy.ndimage.filters documentation

from PIL import Image
import numpy as np
from scipy.ndimage import filters
from matplotlib import pyplot as plt

im = np.array(Image.open('building.jpg').convert('L'))

imx = np.zeros(im.shape)

# sobel derivative filters
# filters.sobel(input image, (1 for x,0 for y derivative), output array)
filters.sobel(im,1,imx)

imy = np.zeros(im.shape)
filters.sobel(im,0,imy)
magnitude = np.sqrt(imx**2+imy**2)

# the drawback of this method is that the derivatives are taken on the scale determined by the image resolution
# gaussian derivative filters are more robust to image noise, and to any scale
# the x and y functions to be convoluted with the image are x and y derivatives of the gaussian kernel

imGx = np.zeros(im.shape)
filters.gaussian_filter(im, (5,5),(0,1), imGx)
# the thrid argument specifies to take the first derivative with respect to the x axis, and 0th derivative with respect to y

imGy = np.zeros(im.shape)
filters.gaussian_filter(im, (5,5),(1,0), imGy)
Gmag = np.sqrt(imGx**2+imGy**2)

plt.figure(1)
plt.subplot(141), plt.imshow(im,cmap='gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(142), plt.imshow(imx,cmap='gray'), plt.title('Sobel Ix')
plt.axis('off')
plt.subplot(143), plt.imshow(imy,cmap='gray'), plt.title('Sobel Iy')
plt.axis('off')
plt.subplot(144), plt.imshow(magnitude,cmap='gray'), plt.title('Magnitude')
plt.axis('off')

plt.figure(2)
plt.subplot(141), plt.imshow(im,cmap='gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(142), plt.imshow(imGx,cmap='gray'), plt.title('Gaussian Ix')
plt.axis('off')
plt.subplot(143), plt.imshow(imGy,cmap='gray'), plt.title('Gaussian Iy')
plt.axis('off')
plt.subplot(144), plt.imshow(Gmag,cmap='gray'), plt.title('Magnitude')
plt.axis('off')
plt.show()

