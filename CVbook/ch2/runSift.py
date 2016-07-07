import sift
import os
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

imname = 'building.jpg'
im1 = np.array(Image.open(imname).convert('L'))
sift.process_image(imname, 'building.sift')
l1, d1 = sift.read_features_from_file('building.sift')

plt.figure()
plt.gray()
sift.plot_features(im1,l1,circle=True)
plt.show()

