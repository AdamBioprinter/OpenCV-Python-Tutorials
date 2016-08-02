import mahotas

class ZernikeMoments:
  
  def __init__(self, radius):
    # store the size of the radius that will be used when computing moments
    self.radius = radius

  def describe(self, image):
    # return the Zerinke moments for the image
    return mahotas.features.zernike_moments(image, self.radius)

# indexing pokemon sprites

import numpy as np
import argparse
import pickle
import glob
import cv2

# construct argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sprites", required = True,
    help = "Path where the sprites will be stored")
ap.add_argument("-i", "--index", required = True,
    help = "Path where the index file will be stored")
args = vars(ap.parse_args())

# intialize our descriptor (Zerinke Moments with a radius of 21
# used to characterize the shape of our pokemon) and our index dictionary
desc = ZernikeMoments(21)
index = {}

# loop over the sprite images
for spritePath in glob.glob(args["sprites"] + "/*.png"):
  
  # parse ot the pokemon name, then load the image and convert to grayscale
  pokemon = spritePath[spritePath.rfind("/") + 1:].replace(".png", "")
  image = cv2.imread(spritePath)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # pad the image with extra white pixels to ensure the edges of the 
  # pokemon are not up against the borders of the image
  image = cv2.copyMakeBorder(image, 15,15,15,15, cv2.BORDER_CONSTANT, value = 255)

  # invert + threshold image
  # the inversion takes place so the foreground is white
  thresh = cv2.bitwise_not(image)
  thresh[thresh > 0] = 255

  # intialize the outline image, find the outermost
  # contours (outline) of the pokemon, the draw it
  outline = np.zeros(image.shape, dtype = "uint8")
  (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
      cv2.CHAIN_APPROX_SIMPLE)
  cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
  cv2.drawContours(outline, [cnts],-1,255,-1)

  # compute Zernike moments to characterize the shape of pokemon outline
  # the update index
  moments = desc.describe(outline)
  index[pokemon] = moments

# write index to file
with open(args["index"], 'wb') as f:
  pickle.dump(index, f)

