# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:15:17 2016

@author: TanMingjun
"""

import numpy as np
import pylab as py
import random
from mpl_toolkits.mplot3d import Axes3D

class random_walk:
    def _init_(self):
        pass
    
    def walk(self):
        self.x=[0]
        self.y=[0]
        self.z=[0]
        self.t=[0]
        while self.t[-1]<1000:
            a=random.randrange(6)
            if a==0:
                x_new=self.x[-1]+1
                y_new=self.y[-1]
                z_new=self.z[-1]
            elif a==1:
                x_new=self.x[-1]-1
                y_new=self.y[-1]
                z_new=self.z[-1]
            elif a==2:
                x_new=self.x[-1]
                y_new=self.y[-1]+1
                z_new=self.z[-1]
            elif a==3:
                x_new=self.x[-1]
                y_new=self.y[-1]-1
                z_new=self.z[-1]
            elif a==4:
                x_new=self.x[-1]
                y_new=self.y[-1]
                z_new=self.z[-1]+1
            else:
                x_new=self.x[-1]
                y_new=self.y[-1]
                z_new=self.z[-1]-1
            t_new=self.t[-1]+1
            self.x.append(x_new)
            self.y.append(y_new)
            self.z.append(z_new)
            self.t.append(t_new)   
                
        return self.x, self.y, self. z
    
        
A=random_walk()
A.walk()
fig=py.figure()
a=fig.add_subplot(111,projection='3d')
a.scatter(A.x,A.y,A.z,color='r',s=10)
a.plot(A.x,A.y,A.z,'g')
a.set_xlabel('x')
a.set_ylabel('y')
a.set_zlabel('z')
a.set_title('Random work: 3D')
py.show()