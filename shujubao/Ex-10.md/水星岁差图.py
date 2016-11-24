# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:28:03 2016

@author: TanMingjun
"""

import math
import pylab as py

GM=4*(math.pi**2)
alpha=0.01
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury，水星最近点
class precession:
    def __init__(self,e=0.206,time=2.,dt=0.0001):
        self.e=e
        self.a=perihelion/(1-e) #从真实最近点，改变离心率
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=math.sqrt((GM*(1-e))/(self.a*(1+e)))*math.sqrt((1+1.2*10**(-6))) #这里我们考虑了行星的质量
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.thetaprecession=[]
        self.timeprecession=[]
        
    def motion_calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+alpha/r**2)*self.X[-1]/r**3)*self.dt #考虑了相对论因素
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+alpha/r**2)*self.Y[-1]/r**3)*self.dt
            newY=self.Y[-1]+newVy*self.dt
            #为了得到下面最近点，0.0014是可调量
            if abs(newX*newVx+newY*newVy)<0.0014 and r<self.a: #对行星近日点的一个定义(约束),表示速度与坐标方向垂直，并且要求是近日点而不是远日点
                theta=math.acos(self.X[-1]/r)*180/math.pi #得出对应的角度
                if (self.Y[-1]/r)<0:
                    theta=360-theta
                theta=abs(theta-180)#之所以要减去180,是因为我们是从最后点出发的，而这要观察最近点的变化
                self.thetaprecession.append(theta)
                self.timeprecession.append(self.T[-1])
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
        
    def plot(self,color='k',slogan=''):
        py.plot(self.X,self.Y,color,label=slogan)
        
    def find_orientation(self,color='',slogan=''):
        py.scatter(self.timeprecession,self.thetaprecession,c=color,label=slogan)
        print (self.thetaprecession)
        print (self.timeprecession)
        
fig=py.figure(figsize=[8,8])
A=precession(e=0.206,time=1)
A.motion_calculate()
A.plot(color='g',slogan=r'e=0.206')
py.xlim(-0.5,0.5)
py.ylim(-0.5,0.5)
py.xlabel("x [AU]")
py.ylabel("y [AU]")
py.title("Simulation of the precession of Mercury")
