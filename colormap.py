#! /usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    #  return x**2+y**3
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),20,alpha=.75,cmap='jet')
plt.colorbar()
C=plt.contour(X,Y,f(X,Y),20,colors='black',linewith=.5)
plt.clabel(C, fmt='%2.1f', colors='w', fontsize=14)
plt.show()
