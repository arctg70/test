#! /usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from PIL import  Image
from matplotlib import cm
from scipy.misc import imsave,imread

mandelbrot_set=imread('mand.jpg')
plt.imshow(mandelbrot_set)
plt.imsave('mandtest.jpg',mandelbrot_set,cmap='jet')
plt.show()
