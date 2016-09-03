#! /usr/bin/env python
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import  Image
from matplotlib import cm
from scipy.misc import imsave
'''
Julia集
'''
# C: 复数
def get_degree(K,C, maxIteration):
    Z = K
    for i in range(0, maxIteration):
        if abs(Z) > 2: break
        Z = Z**2 + C
    return i
# P: 复数, d: 范围
def julia_plot(C, P, d):
    x0, x1, y0, y1 = P[0] - d*16/9, P[0] + d*16/9, P[1] - d, P[1] + d
    y, x = np.ogrid[y0:y1:1080j, x0:x1:1920j]
    z = x + y * 1j
    julia_set = np.frompyfunc(get_degree, 3, 1)(z, C, 512).astype(np.float)
    plt.imsave('julia'+str(abs(P[0]))+'.jpg',julia_set,cmap='jet' )
    plt.imshow(julia_set, extent=[x0, x1, y0, y1])
    #  plt.gca().axis('off')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    #  plt.figure(figsize=(9, 9))
    plt.figure()
    C=-0.8+0.156*1j
    #  C=-0.742 + 0.1*1j
    julia_plot(C,(0.,0.0),1.)
    #  julia_plot(C,(.3467,.2912),.05)
    #  julia_plot(C,(.347566,.289075),.01)
    #  julia_plot(C,(.342871,.28682),.0005)
