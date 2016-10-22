#! /usr/bin/env python
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import fftpack
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

img=np.array(Image.open('julia0.0.jpg').convert('L'))

sig_fft=fftpack.fft2(img)
fshift=np.fft.fftshift(sig_fft)
#fshift=sig_fft
#  noisex=200
#  noisey=290
#  fshift[:noisex,:]=0
#  fshift[:,:noisey]=0
#  fshift[-1*noisex:,:]=0
#  fshift[:,-1*noisey:]=0
fshift2=np.fft.fftshift(fshift)
imgrr=np.abs(fftpack.ifft2(fshift2))


#  print fshift.shape
fft2_orgimg=np.abs(fshift)
fft2_img=np.log(np.abs(fshift))
fig = plt.figure()
#  ax = fig.gca(projection='3d')
#  X = np.arange(0, 470,1)
#  Y = np.arange(0,630, 1)
#  X, Y = np.meshgrid(X, Y)
#  Z = fft2_img[X,Y]
#  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                                 #  linewidth=0, antialiased=False)
#
#  plt.show()
plt.imshow(fft2_img,'gray')
#plt.imshow(fft2_orgimg,'gray')
#  print fft2_orgimg
#
#  plt.imshow(imgrr,'gray')
plt.colorbar()


#  plt.imshow(img,'gray')
#  plt.axis('off')

plt.show()

#  plt.gca().axis('off')

