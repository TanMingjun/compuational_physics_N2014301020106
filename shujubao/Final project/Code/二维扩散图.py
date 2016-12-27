# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:57:41 2016

@author: TanMingjun
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as py
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter 
from copy import deepcopy

class density():
    def __init__(self,t_all):
        self.t_all=t_all
        
    def grid(self):
        self.x = np.linspace(-50,50,101)
        self.y = np.linspace(-50,50,101)
        self.x,self.y = np.meshgrid(self.x,self.y)
        self.d = np.zeros((101,101))
        self.d[50][50]=1
        self.d1 = deepcopy(self.d)
        return self.d1,self.d,self.x,self.y
        
    def diffusion(self):
        for t in range(self.t_all):
            for i in range(101):
                for j in range(101):
                    if i==0 or i==100 or j==0 or j==100:
                        pass
                    else:
                        self.d[i][j]=0.25*(self.d1[i+1][j] + self.d1[i-1][j] + self.d1[i][j+1] + self.d1[i][j-1])
            self.d1=deepcopy(self.d)

        for i in range(101):
                for j in range(101):
                    if i==0 or i==100 or j==0 or j==100:
                        pass
                    else:
                        if self.d[i][j]==0:
                            self.d[i][j]=0.25*(self.d1[i+1][j] + self.d1[i-1][j] + self.d1[i][j+1] + self.d1[i][j-1])

        return self.d

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

A=density(1000)
A.grid()
A.diffusion()
fig = py.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(A.x, A.y, A.d, rstride=1, cstride=1,cmap = cm.jet,
                       linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_ylabel('y(m)')
ax.set_xlabel('x(m)')
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
ax.set_zlabel('density')
ax.set_title('Diffusion in two dimension $t=1000\Delta t$')
py.show()
    