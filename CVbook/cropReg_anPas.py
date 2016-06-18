from PIL import Image
from matplotlib import pyplot as plt
import imtools

pil_im = Image.open('building.jpg')
pil_im = pil_im.resize((800,800))

box = (100,100,400,400) 
region = pil_im.crop(box)

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)

plt.subplot(111), plt.imshow(pil_im)
plt.xticks([]), plt.yticks([])
plt.show()

