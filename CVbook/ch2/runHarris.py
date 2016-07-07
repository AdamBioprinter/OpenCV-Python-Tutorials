import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import filters
import harris
from PIL import Image

im = np.array(Image.open('building.jpg').convert('L'))

harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im,filtered_coords)

