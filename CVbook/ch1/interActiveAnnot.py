# This script shows how to interacti with an image by marking points
# the function that is used to do this is ginput()

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

im = np.array(Image.open('building.jpg'))
plt.imshow(im)
print('Please Click 3 points')
x = plt.ginput(3)
print('you clicked: ', x)
plt.show()

