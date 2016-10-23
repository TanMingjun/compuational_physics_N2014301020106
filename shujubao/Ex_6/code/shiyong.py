# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:45:58 2016

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
        yh=5000#表示目标高度
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
        r=-(self.y[-2]-5000)/(self.y[-1]-5000)
        xl = (self.x[-2]+r*self.x[-1])/(r+1)
        self.x[-1] = xl
        self.y[-1] = 5000
        print (xl)
    def show_results(self):
        x_target=20000
        y_target=5000
        py.plot(x_target, y_target, 'k*',linewidth=10, label='Target')
        py.plot(self.x, self.y,'b')
        py.xlabel('x ($m$)')
        py.ylabel('y ($m$)')
        py.show()
        
a = cannon0(700,58.655)
a.fly()
a.show_results()  
