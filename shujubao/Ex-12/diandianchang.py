# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:03:08 2016

@author: TanMingjun
"""

from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy


# initialize the grid
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
Ex = deepcopy(Z)
Ey = deepcopy(Z)
E = deepcopy(Z)

for i in range(41):
    for j in range(41):
        if i == 0 or i == 40 or j == 0 or j == 40:
            Ex[i][j] = 0
            Ey[i][j] = 0
        elif i==20 and j==20:
            Ex[i][j] = 0
            Ey[i][j] = 0
        else:
            Ex_value = -(Z[i+1][j] - Z[i][j])/0.1
            Ey_value = -(Z[i][j+1] - Z[i][j])/0.1
            Ex[i][j] = Ex_value
            Ey[i][j] = Ey_value

for i in range(41):
    for j in range(41):
        E_value = np.sqrt(Ex[i][j]**2 + Ey[i][j]**2)
        E[i][j] = E_value
            
fig0, ax0 = plt.subplots()
strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color=np.array(E), linewidth=2, cmap=plt.cm.coolwarm_r)
fig0.colorbar(strm.lines)
ax0.set_xlabel('x(m)')
ax0.set_ylabel('y(m)')
ax0.set_title('Electric field')
plt.show()