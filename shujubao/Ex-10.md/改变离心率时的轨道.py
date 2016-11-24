# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:12:02 2016

@author: TanMingjun
"""

import math
import pylab as py
# physical constants
GM=4*(math.pi**2)
alpha=0.0008
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.
# begin the class
class precession:
    def __init__(self,e=0.206,time=2.,dt=0.0001):
        self.e=e
        self.a=perihelion/(1-e)
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=math.sqrt((GM*(1-e))/(self.a*(1+e)))*math.sqrt((1+1.2*10**(-6)))#从最近点出发,这是为了研究最近点，画图时为了美观我们从最远点出发
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.thetaprecession=[0]
        self.timeprecession=[0]
        return None
    def motion_calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+alpha/r**2)*self.X[-1]/r**3)*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+alpha/r**2)*self.Y[-1]/r**3)*self.dt
            newY=self.Y[-1]+newVy*self.dt
            if abs(newX*newVx+newY*newVy)<0.00126 and r<self.a:
                theta=math.acos(self.X[-1]/r)*180/math.pi
                if (self.Y[-1]/r)<0:
                    theta=360-theta
                self.thetaprecession.append(theta)
                self.timeprecession.append(self.T[-1])
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plot(self,color='k',slogan=''):
        py.plot(self.X,self.Y,color,label=slogan)
        return 0
    def find_orientation(self,color='',slogan=''):
        py.scatter(self.timeprecession,self.thetaprecession,color,label=slogan)
        py.plot(self.timeprecession,self.thetaprecession,color,label=slogan)
        py.xlim(0,2)
        py.ylim(0,20)
        print (self.thetaprecession)
        print (self.timeprecession)
        return 0
fig=py.figure(figsize=[8,8])

A=precession(e=0.206,time=5)
A.motion_calculate()
A.plot(color='r',slogan=r'e=0.206')

B=precession(e=0.5,time=5.0)
B.motion_calculate()
B.plot(color='b',slogan='e=0.5')
py.legend(loc='upper right',frameon=False)

C=precession(e=0.8,time=25)
C.motion_calculate()
C.plot(color='g',slogan='e=0.8')
py.legend(loc='upper right',frameon=False)

py.xlim(-1,3)
py.ylim(-2,2)
py.xlabel("x [AU]")
py.ylabel("y [AU]")
py.title("Simulation of the precession of Mercury")
py.legend(loc='upper right',frameon=False)
