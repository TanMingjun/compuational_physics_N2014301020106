# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:00:50 2016

@author: TanMingjun
"""

from __future__ import division
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
class waves:
    def _init_(self):
        self.x = np.linspace(0,1,101)
        self.y=np.exp(-1000*(self.x-0.3)**2) 
        self.y[0] = 0
        self.y[-1] = 0
        line.set_data(self.x,self.y)
    
        return line,

    def iteration(self,num):

        self.x = np.linspace(0,1,101)
        self.y_now=np.exp(-1000*(self.x-0.3)**2) 
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)

        for j in range(num):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)

        return self.y_now

    
    def animate(self,i):

        x = np.linspace(0,1,101)
        y = self.iteration(i)
        line.set_data(x,y)
        return line,
A = waves()
fig = plt.figure()
ax = fig.add_subplot(1,1,1,xlim=(0,1),ylim=(-1,1))
line, = ax.plot([],[],'r',lw=2)
anim1=animation.FuncAnimation(fig, A.animate, init_func=A._init_, frames=200, interval=20)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('wave on a string')
plt.grid(True)
plt.show()