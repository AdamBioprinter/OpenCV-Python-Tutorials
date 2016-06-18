import os
from PIL import Image
import numpy as np

def get_imlist(path):
  """ Return a list of filenames for 
  all jpg images in a directory"""

  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') \
      or f.endswith('.png') or f.endswith('tif')]

def imresize(im,sz):
  """ Resize an image array using PIL."""
  pil_im = Image.fromarray(uint8(im))

  return np.array(pil_im.resize(sz))
