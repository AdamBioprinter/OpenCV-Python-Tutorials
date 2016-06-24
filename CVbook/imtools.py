import os
from PIL import Image
import numpy as np

def get_imlist(path):
  """ Return a list of filenames for 
  all jpg images in a directory"""

  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') \
      or f.endswith('.png') or f.endswith('tif')]

# resize array image using PIL object and convert back to array
def imresize(im,sz):
  """ Resize an image array using PIL."""
  pil_im = Image.fromarray(uint8(im))

  return np.array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
  """ Histogram equalisation of a grayscale image. """
  # get image histogram
  imhist,bins = np.histogram(im.flatten(), nbr_bins, normed=True)

  # cumulative distribution function
  cdf = imhist.cumsum()

  # normalize
  cdf2 = 255*cdf/cdf[-1]

  # use linear interpolation of cdf to find new pixel values
  im2 = np.interp(im.flatten(),bins[:-1],cdf2)

  return im2.reshape(im.shape),cdf,cdf2

def compute_average(imlist):
  """ compute the average of a list of images. """
  # it is important to note this function assumes that all images in imlist are the same size

  # open first image and make into arrau of type float
  averageim = np.array(Image.open(imlist[0]),'f')

  for imname in imlist[1:]:
    try:
      averageim += np.array(Image.open(imname))
    except:
      print(imname + '...skipped')
  averageim /= len(imlist)

  # return average as an unsigned 8 bit integer (0-255)
  return np.array(averageim, 'uint8')
