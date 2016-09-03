#! /usr/bin/env python
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img=np.array(Image.open('mandelbrot.jpg'))
#img_file=cbook.get_sample_data('~/git/testproject/lip.jpg')
#image= plt.imread(img_file)
print img.shape
img[:,:,0]=0     #red
img[:,:,1]=0     #green
#  img[:,:,2]=0     #blue
#  img[:,:,0]=(img[:,:,0]+img[:,:,1]+img[:,:,2])/3
#  img[:,:,1]=img[:,:,0]
#  img[:,:,2]=img[:,:,0]
#plt.figure('lip')
#  print imgclip.shape
plt.imshow(img)
plt.axis('off')

#  pil_im=Image.fromarray(imgclip)
#  pil_im.save('lipclip.png'  )
plt.show()

#  plt.gca().axis('off')
