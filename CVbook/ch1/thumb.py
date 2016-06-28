from PIL import Image
from matplotlib import pyplot as plt
import imtools

pil_im = Image.open('building.jpg')

pil_im2 = Image.open('building.jpg')
pil_im.thumbnail((128,128))

plt.subplot(121), plt.imshow(pil_im)
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(pil_im2)
plt.xticks([]), plt.yticks([])
plt.show()
