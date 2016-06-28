from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

# Read in image and transform to matrix
im = np.array(Image.open('building.jpg'))

# plot image
plt.imshow(im)

# Two ways to turn off the tick marks:
#plt.xticks([])
#plt.yticks([])

# This way, of turning the axis off, also removes the edging "frame" around the image
# looks good for images and should be used
plt.axis('off')

# some points
x = [100,100,400,400]
y = [200,500,200,500]

# plot the points with red star-markers
plt.plot(x,y,'r*')

# line plot connect the first two points
plt.plot(x[:2],y[:2])

# add title and show the plot
plt.title('plotting: "some building"')
plt.show()




