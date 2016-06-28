from PIL import Image
from matplotlib import pyplot as plt
import imtools

# This is a test to see that imtools provides list of images desired
path = '/Users/adamrauff/Desktop/UCD 2014/carpenter research/O.C 2.6.16/CKD study Mouse tibia 781'
lstImages = imtools.get_imlist(path)
print(lstImages)

pil_im = Image.open('building.jpg')

# Using the convert method reads the image in grayscale
pil_im2 = Image.open('building.jpg').convert('L')

plt.subplot(121), plt.imshow(pil_im,cmap="jet")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(pil_im2,cmap="gray")
plt.xticks([]), plt.yticks([])
plt.show()

