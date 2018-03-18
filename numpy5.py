import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('cat.jpg')
img_tinted = img * [1, 0.95, ]