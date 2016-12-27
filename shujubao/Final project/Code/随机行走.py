# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:47:32 2016

@author: TanMingjun
"""

import numpy as np
import pylab as py
import random

class random_walk:
    def _init_(self):
        pass
    def walk(self):
        self.x=[0]
        self.t=[0]
        while self.t[-1]<100:
            a=random.randrange(2)
            if a<0.5:
                x_new=self.x[-1]+1
            else:
                x_new=self.x[-1]-1
            t_new=self.t[-1]+1
            self.x.append(x_new)
            self.t.append(t_new)
            self.N= np.zeros(101)
        return self.x, self.t, self.N
    def plot(self):
        py.scatter(self.t, self.x,color='g',s=20)
        py.plot(self.t, self.N,'k.')
        py.xlim(0,100)
        py.xlabel('step number')
        py.ylabel('x')
        py.title('Random walk in one dimension')
        py.show()
        
A=random_walk()
A.walk()
A.plot()