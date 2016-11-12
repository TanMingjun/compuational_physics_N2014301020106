# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:23:00 2016

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
        self.dt=(3*(math.pi))/1000
        self.F_D=F_D
        self.omiga2=[]
        self.sita2=[]
    
    def calculate(self):
        while self.t[-1]<6000:
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
            
F_D2=[1.35]*128
sita3=[]           
while F_D2[-1]<1.5:
    A=pendulum0(F_D2[-1],0.2)
    A.calculate()
    sita2=[]
    for i in range(301,429):
        A.sita2.append(A.sita[1000*i])
    sita3=sita3+A.sita2
    F_Dnew=[F_D2[-1]+0.00005]*128
    F_D2=F_D2+F_Dnew
            
py.plot(F_D2[0:-128],sita3,'g.')
py.set_title('$\omega$ versus $\\theta$')
py.xlabel('$\\theta$(radians)')
py.ylabel('$\omega$(radians/s)')
py.show()   
