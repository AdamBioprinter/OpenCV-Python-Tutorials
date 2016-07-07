import os
import urllib.request
import urllib.parse
import numpy as np
import requests
import json
import urllib
import sift

url = 'http://www.panoramio.com/map/get_panoramas.php?'
url += 'set=public&from=0&to=20&minx=-77.037564&miny=38.896662&'
url += 'maxx=-77.035564&maxy=38.898662&size=medium&mapfilter=true'

# the response to this is in json format (common data structure for websites)
c = requests.get(url)

print('status code: ',c.status_code)

# get the urls of individual images from JSON
j = c.json()
imurls = []
for im in j['photos']:
  imurls.append(im['photo_file_url'])

imlist = []
featlist = []
# download images
for ur in imurls:
  # image = urllib.URLopener()
  # image = urllib.request.urlretrieve(url, os.path.basename(urllib.parse(url).path))
  image, headers = urllib.request.urlretrieve(ur,os.path.abspath(ur[49:]))
  print('downloading: ',ur)
  imlist.append(str(image))

  sift.process_image(image, str(image+'.sift'))

  featlist.append(str(image+'.sift'))

nbr_images = len(imlist)

matchscores = np.zeros((nbr_images,nbr_images))

for i in range(nbr_images):
  for j in range(i,nbr_images): # only compute upper triangle
    print('comparing ', imlist[i], imlist[j])

    l1 ,d1 = sift.read_features_from_file(featlist[i])
    l2 ,d2 = sift.read_features_from_file(featlist[j])

    matches = sift.match_twosided(d1,d2)

    nbr_matches = sum(matches > 0)
    print('number of matches = ', nbr_matches)
    matchscores[i,j] = nbr_matches

  # copy values
  for i in range(nbr_images):
    for j in range(i+1, nbr_images): # no need to copy diagnoal
      matchscores[j,i] = matchscores[i,j]

# need to process images with sift.py now


# then store images in a list imlist
# store feature files (.sift) in featlist (filenames only)

