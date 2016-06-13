import os

def get_imlist(path):
  """ Return a list of filenames for 
  all jpg images in a directory"""

  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

