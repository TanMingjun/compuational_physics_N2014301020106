# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 17:52:50 2016

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
    def __init__(self,e,time,D, dt=0.0001):#D为误差范围，可根据运行结果合理设置
        self.e=e
        self.a=perihelion/(1-e)
        self.x0=self.a*(1-e)
        self.y0=0
        self.vx0=0
        self.vy0=math.sqrt((GM*(1+e))/(self.a*(1-e)))*math.sqrt((1+1.2*10**(-6)))#从最近点出发,这是为了研究最近点，画图时为了美观我们从最远点出发
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.thetaprecession=[0]
        self.timeprecession=[0]
        self.D=D
        return None
    def motion_calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+alpha/r**2)*self.X[-1]/r**3)*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+alpha/r**2)*self.Y[-1]/r**3)*self.dt
            newY=self.Y[-1]+newVy*self.dt
            if abs(newX*newVx+newY*newVy)<self.D and r<self.a:
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
        py.scatter(self.timeprecession,self.thetaprecession,c=color,label=slogan)
        py.plot(self.timeprecession,self.thetaprecession,c=color,label=slogan)
        py.xlim(0,10)
        py.ylim(0,100)
        print (self.thetaprecession)
        print (self.timeprecession)
        return 0
fig=py.figure(figsize=[8,8])
A=precession(0.206,20,0.00126)
A.motion_calculate()
A.find_orientation(color='r',slogan=r'$eccentricity=0.206$')
A=precession(0.5,20,0.0034)
A.motion_calculate()
A.find_orientation(color='b',slogan=r'$eccentricity=0.5$')
A=precession(0.8,20,0.005)
A.motion_calculate()
A.find_orientation(color='g',slogan=r'$eccentricity=0.8$')
py.xlabel("Time [yr]")
py.ylabel(r"$\theta$ [$\degree$]")
py.title("Orbit Orientation versus Time")