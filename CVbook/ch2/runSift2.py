import sift
import os
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

im1name = 'pic1.JPG'
im2name = 'pic2.JPG'

im1 = np.array(Image.open(im1name).convert('L'))
im2 = np.array(Image.open(im1name).convert('L'))
print('Read images complete')
print('dimensions of images: ')
print('im1: ',im1.shape)
print('im2: ',im2.shape)

sift.process_image(im1name, 'pic1.sift')
sift.process_image(im2name, 'pic2.sift')
print('processed images')
l1, d1 = sift.read_features_from_file('pic1.sift')
l2, d2 = sift.read_features_from_file('pic2.sift')

print('shape of locs var1: ',l1.shape)
print('shape of locs var2: ',l2.shape)
matches = sift.match_twosided(d1,d2)
print('Matches variable dimensions: ',matches.shape)
print('plotting')
plt.figure()
plt.gray()
sift.plot_matches(im1, im2, l1, l2, matches)
plt.show()
