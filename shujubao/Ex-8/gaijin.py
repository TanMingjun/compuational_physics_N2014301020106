# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:35:49 2016

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
            
sub1=py.subplot(221)  
A=pendulum0(1.465,0.2)
A.calculate()
for i in range(300,600):
        A.sita2.append(A.sita[1000*i])
        A.omiga2.append(A.omiga[1000*i])
sub1.plot(A.sita2,A.omiga2,'.',label='$2/3t=2\pi n$')
sub1.set_title('$\omega$ versus $\\theta$')
sub1.legend(loc="upper right",frameon=False)
py.xlabel('$\\theta$(radians)')
py.ylabel('$\omega$(radians/s)')



            
sub2=py.subplot(222)  
A=pendulum0(1.465,0.2)
A.calculate()
for i in range(300,600):
        A.sita2.append(A.sita[1000*i+125])
        A.omiga2.append(A.omiga[1000*i+125])
sub2.plot(A.sita2,A.omiga2,'.',label='$2/3t=2\pi n+\pi /4$')
sub2.set_title('$\omega$ versus $\\theta$')
sub2.legend(loc="upper right",frameon=False)
py.xlabel('$\\theta$(radians)')
py.ylabel('$\omega$(radians/s)')

            
sub3=py.subplot(223)  
A=pendulum0(1.465,0.2)
A.calculate()
for i in range(300,600):
        A.sita2.append(A.sita[1000*i+250])
        A.omiga2.append(A.omiga[1000*i+250])
sub3.plot(A.sita2,A.omiga2,'.',label='$2/3t=2\pi n+\pi /2$')
sub3.set_title('$\omega$ versus $\\theta$')
sub3.legend(loc="upper right",frameon=False)
py.xlabel('$\\theta$(radians)')
py.ylabel('$\omega$(radians/s)')

            
sub4=py.subplot(224)  
A=pendulum0(1.465,0.2)
A.calculate()
for i in range(300,600):
        A.sita2.append(A.sita[1000*i+375])
        A.omiga2.append(A.omiga[1000*i+375])
sub4.plot(A.sita2,A.omiga2,'.',label='$2/3t=2\pi n+3\pi /4$')
sub4.set_title('$\omega$ versus $\\theta$')
sub4.legend(loc="upper right",frameon=False)
py.xlabel('$\\theta$(radians)')
py.ylabel('$\omega$(radians/s)')