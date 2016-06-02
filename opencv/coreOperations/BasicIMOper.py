import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('apple.jpg')

# the common eay to access individual pixels with opencv is by using .itemset to modify a pixel value, and .item to observe a pixel value
img.itemset((100,100,2),255)
print(img.item(100,100,2))

# accesing the shape of the image: returns a tupule of rows, column, channels (if color)
print('Image Shape: ',img.shape)
print('Image Size: ',img.size)
print('Data type: ',img.dtype)

# Image Region of Interest (used with numpy syntax)
R = img[1000:1500, 2000:2500]
img[200:700, 1000:1500] = R

# the following code makes border for images (padding)
constant = cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_CONSTANT,value=[255,0,0])
# The border written above is a constant border that is blue (BGR), for more options check out the tutorials


# the following two lines convert a BGR image (as read by the opencv command imread) to an rgb image, so it can be graphed with matplotlib
[b, g, r] = cv2.split(img)
img2 = cv2.merge([r,g,b])

#this operation can also convert BGR to RGB using numpy
bC = constant[:,:,0] # recall the first channel is indexed at 0
gC = constant[:,:,1]
rC = constant[:,:,2]
constant2 = cv2.merge([rC,gC,bC])

#img2[100100:105] =[[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
cv2.circle(img2,(100,100),40,(0,0,0),-1)
# plt.plot(img)
#plt.imshow(img)

plt.subplot(212), plt.imshow(constant2, cmap='jet'), plt.title('Constant Border')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
