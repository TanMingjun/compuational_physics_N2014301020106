# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:11:02 2016

@author: TanMingjun
"""

import math
import pylab as py
g=9.8
l=1
q=1
ou_D=2
class pendulum0:
    def __init__(self,F_D,sita):
        self.sita=[sita]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def calculate(self):
        while self.t[-1]<20:
            omiga_new=self.omiga[-1]-((g/l)*self.sita[-1]+q*self.omiga[-1]-self.F_D*math.sin(ou_D*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            sita_new=self.sita[-1]+self.omiga[-1]*self.dt
            t_new=self.t[-1]+self.dt
            
            while sita_new > math.pi:
                sita_new -=2*(math.pi)
            while sita_new < -math.pi:
                sita_new +=2*(math.pi)
                
            self.sita.append(sita_new)
            self.t.append(t_new)
    def plot(self):
        py.plot(self.t,self.sita)
        py.xlabel('time [s]')
        py.ylabel('$\theta$ [radians]')
        
A=pendulum0(0.2,0.2)
A.calculate()
A.plot()
py.title('$\theta$ versus time')
py.legend(loc="upper right",frameon=False)
