# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:46:45 2016

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
        vw=10
        while self.y[-1]>=0:
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
        r=-(self.y[-2])/(self.y[-1])
        xl = (self.x[-2]+r*self.x[-1])/(r+1)
        self.x[-1] = xl
        self.y[-1] = 0
        print(a[-1])
        print (xl)
    def show_results(self):
        x_target=20000
        y_target=5000
        py.plot(x_target, y_target, 'k*',linewidth=10, label='Target')
        py.plot(self.x, self.y,'g')
        py.xlabel('x ($m$)')
        py.ylabel('y ($m$)')
        py.show()
        
a=[0]
X1=[]
while a[-1]<=90:
    
    A=cannon0(700,a[-1])
    A.fly()
    A.show_results()
    anew = a[-1] + 1
    a.append(anew)
    
    