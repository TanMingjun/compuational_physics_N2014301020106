# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:40:05 2016

@author: TanMingjun
"""

import pylab as py
import math

class Solar():
    def __init__(self,vy_0):
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.t=[0]
        self.vy=[vy_0]
        self.dt=0.001
    def trajectory(self):
        
        while self.t[-1]<=4:
            r2=(self.x[-1])**2+(self.y[-1])**2
            r=math.sqrt(r2)
            ox=(-4*(math.pi)*(math.pi)*(self.x[-1]))/(r**3)
            oy=(-4*(math.pi)*(math.pi)*(self.y[-1]))/(r**3)
            self.vx.append(self.vx[-1]+ox*(self.dt))
            self.vy.append(self.vy[-1]+oy*(self.dt))
            self.x.append(self.x[-1]+self.vx[-1]*(self.dt))
            self.y.append(self.y[-1]+self.vy[-1]*(self.dt))
            self.t.append(self.t[-1]+(self.dt))
            if math.sqrt((self.x[-1]-1)**2+(self.y[-1])**2)<0.0063and self.y[-1]<0:
                break  
        return self.x,self.y
    def plot(self):
        py.plot(self.x,self.y)
        py.xlabel('x(AU)')
        py.ylabel('y(AU)')
        py.title('Earth orbiting the sun')

A1=Solar(2*math.pi)
A1.trajectory()
A1.plot()
A2=Solar(1.5*math.pi)
A2.trajectory()
A2.plot()
A3=Solar(2.5*math.pi)
A3.trajectory()
A3.plot()
py.scatter([0],[0],s=1000,color='r')
py.show()