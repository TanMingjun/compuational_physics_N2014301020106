# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:29:47 2016

@author: TanMingjun
"""

import math
import pylab as py
# import modules
g=9.8
# set constants
class cannon0:
    def __init__(self,v0,theta):
        self.x0=0
        self.y0=0
        self.v0=v0
        self.theta=theta*math.pi/180
        self.theta1=theta
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.001        
        self.g=9.8
    def fly(self):
        self.x=[self.x0]
        self.y=[self.y0]
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.v=[self.v0]
        yh=5000#目标高度
        vw=10
        while self.y[-1]>=yh or self.vy[-1]>0:
            x_N = self.x[-1] + self.vx[-1] * self.dt
            vx_N = self.vx[-1] - (1-(6.5*(10)**(-3))*self.y[-1]/300)**(2.5)*(math.sqrt((self.vx[-1]-vw)**2+(self.vy[-1])**2))*(4*(10)**(-5))*(self.vx[-1]-vw)*self.dt
            y_N = self.y[-1] + self.vy[-1] * self.dt
            vy_N = self.vy[-1] - self.g*self.dt - (1-(6.5*(10)**(-3))*self.y[-1]/300)**(2.5)*(math.sqrt((self.vx[-1]-vw)**2+(self.vy[-1])**2))*(4*(10)**(-5))*self.vy[-1]*self.dt
            v_N = math.sqrt(vx_N**2 + vy_N**2)
            self.x.append(x_N)
            self.vx.append(vx_N)
            self.y.append(y_N)
            self.vy.append(vy_N)
            self.v.append(v_N)
        #在角度取很小或为90度时，下面一步不成立，应去掉后运行
        r=-(self.y[-2]-5000)/(self.y[-1]-5000)#注意高度
        xl = (self.x[-2]+r*self.x[-1])/(r+1)
        self.x[-1] = xl
        self.y[-1] = 5000
        print(self.theta1)
        print(self.x[-1])
        return self.x[-1]
# Definition of Classes and 
a=[0]
X1=[]
while a[-1]<=90:
    
    A=cannon0(672,a[-1])
    A.fly()
    anew = a[-1] + 1
    a.append(anew)
    X1.append(A.fly())
myfile = open('angle and maximum distance4', 'w')
for i in range(len(a)-1):
    print(a[i], X1[i], file = myfile)
myfile.close()
py.plot(a[0:-1],X1)
x=[0,90]
y=[20000,20000]
py.plot(x,y)