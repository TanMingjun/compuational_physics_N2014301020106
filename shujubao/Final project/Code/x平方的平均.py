# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:54:25 2016

@author: TanMingjun
"""

import numpy as np
import pylab as py
import random

class random_walk:
    def _init_(self):
        pass
    def walk(self):
        self.i=[0]
        self.x_2ave=np.zeros(101)
        while self.i[-1]<10000:
            self.x=[0]
            self.t=[0]
            self.x_2=[0]
            while self.t[-1]<100:
                a=random.randrange(4)
                if a<0.5:
                    x_new=self.x[-1]+1
                else:
                    x_new=self.x[-1]-1
                t_new=self.t[-1]+1
                self.x.append(x_new)
                self.x_2.append(x_new**2)
                self.t.append(t_new)   
            for l in range(101):
                self.x_2ave[l]=(self.x_2ave[l]*self.i[-1]+self.x_2[l])/(self.i[-1]+1)
            self.i.append(self.i[-1]+1)
        return self.x_2ave, self.t
    def plot(self):
        para = np.polyfit(self.t, self.x_2ave,2)
        poly = np.poly1d(para)
        y_fit = poly(self.t)
        py.plot(self.t, y_fit, 'y', label = 'fit line')
        py.scatter(self.t, self.x_2ave,color='k',s=2)
        py.xlim(0,100)
        py.xlabel('step number(=time)')
        py.ylabel('$<x^2>$')
        py.title('Random walk in one dimension')
        py.show()
        
A=random_walk()
A.walk()
A.plot()