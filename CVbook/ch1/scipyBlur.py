# gausssian blurring is an example of image convolution
# the image is convolved with a gaussian kernel to create a blurred version
from PIL import Image
import numpy as np
from scipy.ndimage import filters
from matplotlib import pyplot as plt

im = np.array(Image.open('building.jpg').convert('L'))

# The second argument defines the standard deviation in the gaussian kernel
im2 = filters.gaussian_filter(im,5)
im3 = filters.gaussian_filter(im,10)

plt.figure(1)
plt.subplot(131), plt.imshow(im, cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(132), plt.imshow(im2, cmap='gray'),plt.title('std = 5 Blur')
plt.axis('off')
plt.subplot(133), plt.imshow(im3, cmap='gray'),plt.title('std = 10 Blur')
plt.axis('off')

# for color images, apply gaussian blur to each color channel
imC = np.array(Image.open('building.jpg'))
imC2 = np.zeros(imC.shape)
for i in range(3):
  imC2[:,:,i] = filters.gaussian_filter(imC[:,:,i],5)
# This line forces the pixel values to be 8 bit representation, the same as the original image
imC2 = np.uint8(imC2)
# keep in mind if you don't know the data type of an image, or you are handling multiple ones, it is better to first determine the data type using .dtype() method on the original image
# then use appropriate conversion on the processed image

plt.figure(2)
plt.subplot(121), plt.imshow(imC), plt.title('Original Image')
plt.axis('off')
plt.subplot(122), plt.imshow(imC2), plt.title('Blurred Image')
plt.axis('off')
plt.show()
