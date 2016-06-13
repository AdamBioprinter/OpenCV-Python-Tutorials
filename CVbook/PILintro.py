from PIL import Image
from matplotlib import pyplot as plt

pil_im = Image.open('building.jpg')

# Using the convert method reads the image in grayscale
pil_im2 = Image.open('building.jpg').convert('L')

plt.subplot(121), plt.imshow(pil_im,cmap="jet")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(pil_im2,cmap="gray")
plt.xticks([]), plt.yticks([])
plt.show()

