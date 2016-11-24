# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:22:17 2016

@author: TanMingjun
"""

import math
import pylab as py
# physical constants
GM=4*(math.pi**2)

# begin the class
class Solar1:
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
    
class Solar2():
    def __init__(self,a, e, M_P, M_S):
        self.a=a
        self.e=e
        self.x=[a]
        self.y=[0]
        self.theta=[0]
        self.dtheta=0.0001
        self.M_P=M_P
        self.M_S=M_S
    def run(self):
        while self.theta[-1]<2*math.pi:
            self.r=self.a*(1-self.e*self.e)/(1-self.e*(math.cos(self.theta[-1])))
            x_new=self.r*(math.cos(self.theta[-1]))#我们取焦点为原点，故平移了一下self.e*self.a
            y_new=self.r*(math.sin(self.theta[-1]))
            self.x.append(x_new)
            self.y.append(y_new)
            self.theta.append(self.theta[-1]+self.dtheta)
    
    def plot(self,color=''):
        py.plot(self.x,self.y,color)
        
fig=py.figure(figsize=[8,8])
A1=Solar1(0.007,0.72,4.9)
A1.motion_calculate()
A1.plot()

A2=Solar1(0.017,1,6)
A2.motion_calculate()
A2.plot()

A=Solar2(0.72,0.017,4.9,198910)
A.run()
A.plot(color='r--')

A=Solar2(1,0.007,6,198910)
A.run()
A.plot(color='y--')

py.scatter([0],[0],s=100,color='r')
py.show