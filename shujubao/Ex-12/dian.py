# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 23:47:46 2016

@author: TanMingjun
"""

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter 

# initialize the grid
#这个步骤就是定义了一个初始条件，类似一个矩阵，当然可以用while句式
class potential():
    def __init__(self):
        pass
    def grid_production(self):
        self.grid = []
        for i in range(41):    
            self.row_i = []
            for j in range(41):
                if i == 0 or i == 40 or j == 0 or j == 40:
                    self.voltage = 0
                elif i==20 and j==20:
                    self.voltage = 1
                else:
                    self.voltage = 0
                self.row_i.append(self.voltage)
            self.grid.append(self.row_i)
        return self.grid
# define the update_V function (Gauss-Seidel method)

    def update_V(self):

        self.delta_V = 0
        for i in range(41):    
            for j in range(41):
                if i == 0 or i == 40 or j == 0 or j == 40:
                    pass
                elif i==20 and j==20:
                    pass
                else:
                    voltage_new = (self.grid[i+1][j]+self.grid[i-1][j]+self.grid[i][j+1]+self.grid[i][j-1])/4
                    voltage_old = self.grid[i][j]
                    self.delta_V += abs(voltage_new - voltage_old)
                    self.grid[i][j] = voltage_new

        return self.grid, self.delta_V

# define the Laplace_calculate function

    def Laplace_calculate(self):

        self.epsilon = 10**(-6)*40**2
        self.grid_init = self.grid
        self.delta_V = 0
        self.N_iter = 0

        while self.delta_V >= self.epsilon or self.N_iter <= 100:
            self.grid_new, self.delta_V = self.update_V()
            self.grid = self.grid_new
            self.N_iter += 1

        return self.grid_new
    
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

A=potential()
A.grid_production()
A.update_V()
A.Laplace_calculate()
x = np.linspace(-1,1,41)
y = np.linspace(-1,1,41)
X, Y = np.meshgrid(x, y)
Z =A.Laplace_calculate()

 

CS = plt.contour(X,Y,Z,12)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap = cm.jet,
                       linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_ylabel('y(m)')
ax.set_zlabel('voltage(V)')
ax.set_title('voltage distribution')

plt.show()