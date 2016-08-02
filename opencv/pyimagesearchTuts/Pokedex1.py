# This is a tutorial that is posted on pyimagesearch website
# the first of 2 of 6 segments
# This segment deals with scarping the database together

from bs4 import BeautifulSoup 
import argparse
import requests

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pokemon-list", required = True,
    help = "Path to where the raw Pokemon HTML file resides")
ap.add_argument("-s", "--sprites", required = True,
    help = " Path where the sprites will be stored")
args = vars(ap.parse_args())

# construct the soup and initialize the list of pokemon names
soup = BeautifulSoup(open(args["pokemon_list"]).read())
names = []

# loop pver all link elements
for link in soup.findAll("a"):
  # update the list of pokemon names
  names.append(link.text)


# loop over pokemon names
for name in names:

  # intialize the parsed name as just the lowercase version of the name
  parsedName = name.lower()

  # remove apostrophes
  parsedName = parsedName.replace("'","")

  # replace periods + space with dash (i.e Mr. Mime = mr-mime)
  parsedName = parsedName.replace(". ", "-")

  # handle the case for Nidoran (female)
  if name.find(u'\u2640') != -1:
    parsedName = "nidoran-f"

  # handle the case for Nidoran (male)
  if name.find(u'\u2642') != -1:
    parsedName = "nidoran-m"

  # downloading the pokemon sprite
  print("[x] downloading %s" %(name))
  url = "http://img.pokemondb.net/sprites/red-blue/normal/%s.png" %(parsedName)
  r = requests.get(url)

  # if the status conde is not 200, ignore the sprite
  if r.status_code != 200:
    print("[x] error donwloading %s" %(name))
    continue
  # write the sprite to file
  f = open("%s%s.png" %(args['sprites'], name.lower()), "wb")
  f.write(r.content)
  f.close()




  


