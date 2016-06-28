# this script illustrates data types upon creation of a numpy array from an image
# an array is restricted to having all elements of the same type, unlike a list

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

im = np.array(Image.open('building.jpg'))

print(im.shape, im.dtype)

# in this line, we import the same image, convert it to grayscale, and then specify the data type to be float
im2 = np.array(Image.open('building.jpg').convert('L'),'f')

print(im2.shape, im2.dtype)

# accessing array with indexes i,j,k
i = 24 # x coordinate (rows)
j = 203 # cols
k = 2 # color channel (Green) R = 0 B = 1 G = 2

value = im[i,j,k]
print(value)

im[i,:] = im[j,:] # set the values of row i with values from row j
im[:,i] = 100 # set all values in column i to 100
Sum = im[:100,:50].sum() # stor the sum of the values of the first 100 rows and 50 
                        #columns in Sum
imBox = im[50:100,50:100] # rows 50-100, columns 50-100 (100 not included)
imIMean = im[i].mean() # average of row i
im[:,-1]                # last column
im[-2,:] # second to last row

