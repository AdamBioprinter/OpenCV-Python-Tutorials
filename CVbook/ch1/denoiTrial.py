import numpy as np
from scipy.ndimage import filters
import rof
from matplotlib import pyplot as plt
from PIL import Image

# now lets see how the ROF algorithm handles real images
im2 = np.array(Image.open('Image 4_z34.tif'))
U2, T2 = rof.denoise(im2, im2)

plt.subplot(121), plt.imshow(im2,'gray'), plt.title('Original Image')
plt.axis('equal'), plt.axis('off')
plt.subplot(122), plt.imshow(U2,'gray'), plt.title('ROF denoising')
plt.axis('equal'), plt.axis('off')

plt.show()
