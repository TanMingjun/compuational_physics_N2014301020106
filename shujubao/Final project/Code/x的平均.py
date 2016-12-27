# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:14:41 2016

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
        self.x_ave=np.zeros(101)
        while self.i[-1]<10000:
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
            for l in range(101):
                self.x_ave[l]=(self.x_ave[l]*self.i[-1]+self.x[l])/(self.i[-1]+1)
            self.i.append(self.i[-1]+1)
        return self.x_ave, self.t
    def plot(self):
        py.scatter(self.t, self.x_ave,color='pink',s=20)
        py.xlim(0,100)
       
        py.xlabel('step number')
        py.ylabel('<x>')
        py.title('Random walk in one dimension')
        py.show()
        
A=random_walk()
A.walk()
A.plot()