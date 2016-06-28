from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import imtools

im = np.array(Image.open('building.jpg').convert('L'))
im2,cdf,cdf2 = imtools.histeq(im)

plt.figure(1)
plt.subplot(131), plt.hist(im.flatten(), 256, normed=True)
plt.title('histogram of original image'), plt.xlabel('pixel depth') 
plt.ylabel('frequency')
plt.subplot(132), plt.plot(cdf)
plt.title('cdf')
plt.subplot(133), plt.plot(cdf2)
plt.title('normalized cdf')

plt.figure(2)
plt.subplot(121), plt.imshow(im, cmap='gray'), plt.axis('off')
plt.title('original image')
plt.subplot(122), plt.imshow(im2, cmap='gray'), plt.axis('off')
plt.title('processed image')
plt.show()

