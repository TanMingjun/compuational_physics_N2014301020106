# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:52:07 2016

@author: TanMingjun
"""

from __future__ import division
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
class diffusion:
    def _init_(self):
        self.x = np.linspace(-1000,1000,2001)
        self.d= list(np.zeros(1000)) + list(np.ones(1)) + list(np.zeros(1000))
        line.set_data(self.x,self.d)
        return line,

    def iteration(self,num):

        self.x = np.linspace(-1000,1000,2001)
        self.d_now=list(np.zeros(1000)) + list(np.ones(1)) + list(np.zeros(1000)) 
        self.d_new = np.zeros(2001)

        for j in range(int(num/20)):
            for i in range(2001):
                if i== 0 or i== 2000:
                    pass
                else:
                    self.d_new[i] = 0.5*(self.d_now[i+1] + self.d_now[i-1])
            self.d_now = deepcopy(self.d_new)
        for i in range(2001):
            if i==0 or i==2000:
                pass
            else:
                if self.d_now[i]==0:
                    self.d_new[i] = 0.5*(self.d_now[i-1] + self.d_now[i+1])
                
        return self.d_new

    
    def animate(self,i):

        x = np.linspace(-1000,1000,2001)
        y = self.iteration(i)
        line.set_data(x,y)
        return line,
A = diffusion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1,xlim=(-50,50),ylim=(0,1))
line, = ax.plot([],[],'b',lw=2)
anim1=animation.FuncAnimation(fig, A.animate, init_func=A._init_, frames=500, interval=20)
plt.xlabel('x')
plt.ylabel('density')
plt.title('Diffusion in one dimension')
plt.grid(True)
plt.show()