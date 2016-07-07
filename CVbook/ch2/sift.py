import os
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):
  """ Process an image and save the result in a file."""
  
  # Note this is only true at July 3rd 2016, when the VLFeat folder is located in this place on adam's computer 
  filePath = '/Users/adamrauff/vlfeat-0.9.20/bin/maci64/'
  
  if imagename[-3:] != 'pgm' :
    # creage a pgm file
    im = Image.open(imagename).convert('L')
    im.save('tmp.pgm')
    imagename = 'tmp.pgm'

  cmmd = str(filePath+"sift "+imagename+" --output="+resultname+ " " 
      +params)
  os.system(cmmd)
  # print('processed', imagename, 'to', resultname)

def read_features_from_file(filename):
  """ Read feature properties and return in matrix form. """

  f = np.loadtxt(filename)
  return f[:,:4], f[:,4:] # feature locations, descriptors

# this function is used to write results back to feature file if you midift the descriptors

def write_featrues_to_file(filename, locs, desc):
  """ Sace feature location and descriptor to file. """

  np.savetxt(filename, np.hstack((locs,desc)))

def plot_features(im,locs,circle=False):
  """ Show image with features.
      Input: im (image as array), 
             locs (row,col, scale, orientation of each feature). """

  def draw_circle(c,r):
    t = np.arange(0,1.01,0.1)*2*np.pi
    x = r*np.cos(t) + c[0]
    y = r*np.sin(t) + c[1]
    plt.plot(x,y,'b',linewidth=2)

  plt.imshow(im)
  if circle:
    for p in locs:
      draw_circle(p[:2],p[2])
  else:
    plt.plot(locs[:,0],locs[:,1],'ob')
  plt.axis('off')

def match(desc1, desc2):
  """ For each descriptor in the first image,
    select its match in the second image.
    input: desc1 (descriptors for the first image),
    desc2 (same for second image). """


  desc1 = np.array([d/np.linalg.norm(d) for d in desc1])
  desc2 = np.array([d/np.linalg.norm(d) for d in desc2])

  dist_ratio = 0.6
  desc1_size = desc1.shape

  matchscores = np.zeros((desc1_size[0],1),'int')
  desc2t = desc2.T # precompute matrix transpose
  for i in range(desc1_size[0]):
    dotprods = np.dot(desc1[i,:], desc2t) # vector of dot products
    dotprods = 0.9999*dotprods
    # note that each feature in image 1 is matches to all features in the 
    # second image
    
    #inverse cosine and sort, return index for features in second image
    indx = np.argsort(np.arccos(dotprods))

    #check if nearest neighbor has angle less than dist_ratio times 2nd
    if np.arccos(dotprods)[indx[0]] < dist_ratio*np.arccos(dotprods)[indx[1]]:
      matchscores[i] = int(indx[0])
  
  # print('matchscores: ',matchscores)
  return matchscores

def match_twosided(desc1, desc2):
  """ Two sided symmetric version of match(). """

  matches_12 = match(desc1, desc2)
  matches_21 = match(desc2, desc1)

  ndx_12 = np.where(matches_12 >= 0)[0]

  # print('nonzero matches:: ',ndx_12)
  # remove matches that are not stmmetrix 
  for n in ndx_12:
    if matches_21[int(matches_12[n])] != n:
      matches_12[n] = -1 
  
  # print('nonzero filtered matches:: ',matches_12.nonzero()[0])
  return matches_12

def appendimages(im1,im2):
  """ Return a new image that appends the two images side by side. """

  # select the image with the fewest rows and fill in enough empty rows
  rows1 = im1.shape[0]
  rows2 = im2.shape[0]

  if rows1 < rows2:
    im1 = np.concatenate((im1,np.zeros((rows2-rows1, im1.shape[1]))),axis=0)
  elif rows1 > rows2:
    im2 = np.concatenate((im2,np.zeros((rows1-rows2, im2.shape[1]))),axis=0)

  # if none of these cases, they are equal, no filling needed.

  return np.concatenate((im1,im2),axis=1)

def plot_matches(im1,im2,locs1, locs2, matchscores, show_below=True):
  """ Show a figure with lines joining the accepted matches

  input: im1, im2 (images as arrays), locs1, locs2 (feature locations),
         marchscores (as output from match()),
         show_below (if images should be shown below matches). """

  im3 = appendimages(im1,im2)
  if show_below:
    im3 = np.vstack((im3,im3))

  plt.imshow(im3)

  cols1 = im1.shape[1]
  for i,m in enumerate(matchscores):
    if m>0:
      print('i, m: ',i,' ',m)
      plt.plot([locs1[i,1], locs2[m,1]+cols1], [locs1[i,0], locs2[m,0]],
          'c')
  plt.axis('off')
