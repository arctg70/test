#! /usr/bin/env python
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import  Image
from matplotlib import cm
from scipy.misc import imsave
'''
Mandelbrot集
'''
# C: 复数
def get_degree(C, maxIteration):
    Z = C
    for i in range(0, maxIteration):
        if abs(Z) > 2: break
        Z = Z**2 + C
    return i
# P: 复数, d: 范围
def mandelbrot_plot(P, d):
    x0, x1, y0, y1 = P[0] - d*16/9, P[0] + d*16/9, P[1] - d, P[1] + d
    y, x = np.ogrid[y0:y1:1080j, x0:x1:1920j]
    c = x + y * 1j
    mandelbrot_set = np.frompyfunc(get_degree, 2, 1)(c, 1024).astype(np.float)
    plt.imsave('mand'+str(abs(P[0]))+'.jpg',mandelbrot_set,cmap='jet' )
    plt.imshow(mandelbrot_set, extent=[x0, x1, y0, y1])
    plt.gca().axis('off')
    #  plt.colorbar()
    plt.show()

if __name__ == '__main__':
    #  plt.figure(figsize=(9, 9))
    plt.figure()
    #  mandelbrot_plot((-0.5, 0), 1.5)
    #  mandelbrot_plot((0.408602, 0.322581), 0.02)
    #  mandelbrot_plot((0.406738, 0.321649), 0.004)
    #  mandelbrot_plot((0.404401, 0.319584), 0.012)
    #  mandelbrot_plot((0.399025, 0.321304), 0.012)
    #  mandelbrot_plot((0.402588,  0.325519), 0.003)
    mandelbrot_plot((0.403231, 0.324479), 0.00005)
    #  mandelbrot_plot((-1.15237, 0.27957), 0.03)
    #  mandelbrot_plot((-1.12291, 0.27914), 0.02)
    #  mandelbrot_plot((0.2, 0.6), 0.5)
