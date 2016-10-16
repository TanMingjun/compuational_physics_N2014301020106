# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:35:02 2016

@author: TanMingjun
"""

import math
import pylab as py
class cannon_trajectory:
    a=float(input('angle'))
    def __init__(self, v_x = 700*math.cos(a*math.pi/180), v_y = 700*math.sin(a*math.pi/180), time_step = 0.05):
        self.x = [0.0]
        self.y = [0.0]
        self.vx = [v_x]
        self.vy = [v_y]
        self.dt = time_step
        self.g = 9.8
        self.v = [700.0]
    def calculate(self):
         while self.y[-1] >= 0:
            x_N = self.x[-1] + self.vx[-1] * self.dt
            vx_N = self.vx[-1] 
            y_N = self.y[-1] + self.vy[-1] * self.dt
            vy_N = self.vy[-1] - self.g*self.dt 
            v_N = math.sqrt(vx_N**2 + vy_N**2)
            self.x.append(x_N)
            self.vx.append(vx_N)
            self.y.append(y_N)
            self.vy.append(vy_N)
            self.v.append(v_N)
         r=-self.y[-2]/self.y[-1]
         xl = (self.x[-2]+r*self.x[-1])/(r+1)
         yl = 0
         self.x[-1] = xl
         self.y[-1] = yl    
       
    def show_results(self):
        py.plot(self.x, self.y)
        py.xlabel('x ($m$)')
        py.ylabel('y ($m$)')
        py.show()
a = cannon_trajectory()
a.calculate()
a.show_results()