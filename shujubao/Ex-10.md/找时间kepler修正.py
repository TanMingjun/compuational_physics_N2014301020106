# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:11:21 2016

@author: TanMingjun
"""

import math
import pylab as py
# physical constants
GM=4*(math.pi**2)

# begin the class
class Solar:
    def __init__(self,e, a, M_P, time=30.,dt=0.0001):
        self.e=e
        self.a=a
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=math.sqrt((GM*(1-e))/(self.a*(1+e)))*math.sqrt(1+M_P/198910)#从最近点出发,这是为了研究最近点
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        
    def motion_calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*self.X[-1]/r**3)*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*self.Y[-1]/r**3)*self.dt
            newY=self.Y[-1]+newVy*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
            if math.sqrt((self.X[-1]-self.X[0])**2+(self.Y[-1])**2)<0.00080 and self.Y[-1]<0:
                print('k')
                print((self.T[-1])**2/(self.a**3))
                break     
        
    def plot(self):
        py.plot(self.X,self.Y)
        py.xlim(-12,16)
        py.ylim(-12,16)

fig=py.figure(figsize=[8,8])
A1=Solar(0.007,0.72,4.9)
A1.motion_calculate()
A1.plot()
A2=Solar(0.017,1,6)
A2.motion_calculate()
A2.plot()
A3=Solar(0.093,1.52,0.66)
A3.motion_calculate()
A3.plot()
A4=Solar(0.048,5.2,1900)
A4.motion_calculate()
A4.plot()
A5=Solar(0.056,9.54,570)
A5.motion_calculate()
A5.plot()
py.scatter([0],[0],s=100,color='r')
py.show()        