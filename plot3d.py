from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    R = np.sqrt(x**2 + y**2)
    return np.sin(R)

    #  return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-3, 3, 0.05)
Y = np.arange(-3, 3, 0.05)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
#  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#  linewidth=0, antialiased=False)
#  ax.set_zlim(-1.01, 1.01)
#  ax.zaxis.set_major_locator(LinearLocator(10))
#  ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#  fig.colorbar(surf, shrink=0.5, aspect=5)

surf = ax.contourf(X, Y, Z, 256, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, 16, colors='black', linewith=.5)
ax.clabel(cset, fmt='%2.1f', colors='w', fontsize=14)

#  xs=np.linspace(-5,5,50)
#  ys=np.linspace(-5,5,50)
#  X,Y=np.meshgrid(xs,ys)
#  Z=f(X,Y)
#  wframe=ax.plot_wireframe(X,Y,Z,rstride=2,cstride=2,color='black')

plt.show()
