#! /usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)


pl.plot(X, C, color="blue", linewidth=2.5, linestyle="-",label='cosX')
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="-",label='sinX')

pl.xlim(X.min() * 1.1, X.max() * 1.1)
pl.ylim(C.min() * 1.1, C.max() * 1.1)

pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
pl.yticks([-1, 0, +1])

pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

pl.yticks([-1, 0, +1],
    [r'$-1$', r'$0$', r'$+1$'])

ax = pl.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

pl.legend(loc='upper left')

t = 2 * np.pi / 3
pl.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
pl.scatter([t, ], [np.cos(t), ], 50, color='blue')
pl.plot([t,t],[0,np.sin(t)],color='red',linewidth=2.5,linestyle="--")
pl.scatter([t,t],[np.sin(t),np.sin(t)],50,color='red')

pl.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t, np.sin(t)), xycoords='data',
    xytext=(+10, +30), textcoords='offset points', fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
pl.annotate(r'$cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t,np.cos(t)),fontsize=16,
    xycoords='data',xytext=(+10,+30),textcoords='offset points',
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
pl.show()
a=np.linspace(0,2*np.pi,360*4)
x=np.sin(a)
y=np.cos(a)
pl.plot(x,y)
pl.show()

