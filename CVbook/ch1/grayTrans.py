# After reading in an image as an array, we can perform any operations we would like on it

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im = np.array(Image.open('building.jpg').convert('L'))

im2 = 255 - im # invert image

im3 = (100.0/255)*im + 100 # clamp to interval 100-200

im4 = 255.0*(im/255.0)**2

print('im', int(im.min()), int(im.max()))
print('im2', int(im2.min()), int(im2.max()))
print('im3', int(im3.min()), int(im3.max()))
print('im4', int(im4.min()), int(im4.max()))

plt.subplot(221), plt.imshow(im, cmap='gray'),plt.axis('off'), plt.title('Original Image')
plt.subplot(222), plt.imshow(im2, cmap='gray'),plt.axis('off'), plt.title('Inverted Image')
plt.subplot(223), plt.imshow(im3, cmap='gray'),plt.axis('off'), plt.title('Inerval 100 to 200')
plt.subplot(224), plt.imshow(im4, cmap='gray'),plt.axis('off'), plt.title('Sqaured')
plt.show()

# The reverse of the array transformation, converting a numpy array back to PIL image object, canv be done with the Image.fromarray() command.
# this reuquires the array to be of type "uint8" (unsigned 8 bit integer, 0-255)
# in the examples above, we changes im3 and im4 to be float, to conver it back, use uint8(im)

# ex: pil_im = Image.fromarray(uint8(im))
