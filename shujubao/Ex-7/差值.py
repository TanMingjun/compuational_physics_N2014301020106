# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:54:52 2016

@author: TanMingjun
"""

import math
import pylab as py
g=9.8
l=9.8
q=0.5
ou_D=2/3
class pendulum0:
    def __init__(self,F_D,sita):
        self.sita=[sita]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def calculate(self):
        while self.t[-1]<150:
            omiga_new=self.omiga[-1]-((g/l)*(math.sin(self.sita[-1]))+q*self.omiga[-1]-self.F_D*math.sin(ou_D*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            sita_new=self.sita[-1]+self.omiga[-1]*self.dt
            t_new=self.t[-1]+self.dt
            
            while sita_new > math.pi:
                sita_new -=2*(math.pi)
            while sita_new < -math.pi:
                sita_new +=2*(math.pi)
            
            self.sita.append(sita_new)
            self.t.append(t_new)
        return self.sita
    def plot(self,color):
        py.plot(self.t,self.sita,'b')
        py.xlable('time [s]')
        py.ylable('$\theta$ [radians]')
        
class pendulum1:
    def __init__(self,F_D,sita):
        self.sita=[sita]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def calculate(self):
        while self.t[-1]<150:
            omiga_new=self.omiga[-1]-((g/l)*(math.sin(self.sita[-1]))+q*self.omiga[-1]-self.F_D*math.sin(ou_D*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            sita_new=self.sita[-1]+self.omiga[-1]*self.dt
            t_new=self.t[-1]+self.dt
            
            while sita_new > math.pi:
                sita_new -=2*(math.pi)
            while sita_new < -math.pi:
                sita_new +=2*(math.pi)
                
            self.sita.append(sita_new)
            self.t.append(t_new)
        return self.t
    def plot(self,color):
        py.plot(self.t,self.sita,'b')
        py.xlable('time [s]')
        py.ylable('$\theta$ [radians]')

A1=pendulum0(0.5,0.2)
M=A1.calculate()
A2=pendulum0(0.5,0.201)
N=A2.calculate()
A=pendulum1(0.5,0.2)
T=A.calculate()
for i in range(len(M)):
    N[i]=math.sqrt((N[i]-M[i])**2)
py.plot(T,N)


py.show()