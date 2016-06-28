import numpy as np
from scipy.ndimage import filters
import rof
from matplotlib import pyplot as plt
from PIL import Image

# create a synthetic image with noise
im = np.zeros((500,500))
im[100:400 , 100:400] = 128
im[200:300, 200:300] = 255
im = np.array(im, 'uint8')
# add some noise
im = im + 30*np.random.standard_normal((500,500))


U, T = rof.denoise(im, im)
G = filters.gaussian_filter(im,10)

# plot result
plt.figure(1)
plt.subplot(131), plt.imshow(im,'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(132), plt.imshow(G,'gray'), plt.title('Gaussian Filter')
plt.axis('off')
plt.subplot(133), plt.imshow(U,'gray'), plt.title('ROF denoising')
plt.axis('off')

# now lets see how the ROF algorithm handles real images
im2 = np.array(Image.open('building.jpg').convert('L'))
U2, T2 = rof.denoise(im2, im2)

G2 = filters.gaussian_filter(im2,10)

plt.figure(2)
plt.subplot(131), plt.imshow(im2,'gray'), plt.title('Original Image')
plt.axis('equal'), plt.axis('off')
plt.subplot(132), plt.imshow(G2,'gray'), plt.title('Gaussian Filter')
plt.axis('equal'), plt.axis('off')
plt.subplot(133), plt.imshow(U2,'gray'), plt.title('ROF denoising')
plt.axis('equal'), plt.axis('off')

plt.show()
