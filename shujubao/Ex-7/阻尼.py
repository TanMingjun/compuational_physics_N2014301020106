# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:38:55 2016

@author: TanMingjun
"""
import math
import pylab as py
g=9.8
l=1
q=1
ou_D=2
class pendulum0:
    def __init__(self,q,sita):
        self.sita=[sita]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.q=q
    def calculate(self):
        while self.t[-1]<10:
            omiga_new=self.omiga[-1]-((g/l)*self.sita[-1]+self.q*self.omiga[-1])*self.dt
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
        
A=pendulum0(1,0.2)
A.calculate()
A.plot()
py.title('$\theta$ versus time')
py.legend(loc="upper right",frameon=False)

A1=pendulum0(5,0.2)
A1.calculate()
A1.plot()
py.title('$\theta$ versus time')
py.legend(loc="upper right",frameon=False)

A2=pendulum0(10,0.2)
A2.calculate()
A2.plot()
py.title('$\theta$ versus time')
py.legend(loc="upper right",frameon=False)


py.show()


    