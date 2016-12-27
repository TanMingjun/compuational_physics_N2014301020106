# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 21:53:54 2016

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
        self.r_2ave=np.zeros(101)
        while self.i[-1]<5000:
            self.x=[0]
            self.y=[0]
            self.z=[0]
            self.t=[0]
            self.r_2=[0]
            while self.t[-1]<100:
                a=random.randrange(2)
                b=random.randrange(2)
                c=random.randrange(2)
                if a==0:
                    x_new=self.x[-1]+1
                elif a==1:
                    x_new=self.x[-1]-1
                if b==0:
                    y_new=self.y[-1]+1
                elif b==1:
                    y_new=self.y[-1]-1
                if c==0:
                    z_new=self.z[-1]+1
                elif c==1:
                    z_new=self.z[-1]-1
                t_new=self.t[-1]+1
                r_2_new=x_new**2+y_new**2+z_new**2
                self.x.append(x_new)
                self.y.append(y_new)
                self.z.append(z_new)
                self.r_2.append(r_2_new)
                self.t.append(t_new)   
            for l in range(101):
                self.r_2ave[l]=(self.r_2ave[l]*self.i[-1]+self.r_2[l])/(self.i[-1]+1)
            self.i.append(self.i[-1]+1)
        return self.r_2ave, self.t
    def plot(self):
        para = np.polyfit(self.t, self.r_2ave,1)
        poly = np.poly1d(para)
        y_fit = poly(self.t)
        py.plot(self.t, y_fit, 'r', label = 'fit line')
        py.scatter(self.t, self.r_2ave,color='k',s=2)
        py.xlim(0,100)
        py.ylim(0,300)
        py.xlabel('step number(=time)')
        py.ylabel('$<r^2>$')
        py.title('Random walk in three dimension')
        py.show()
        
A=random_walk()
A.walk()
A.plot()