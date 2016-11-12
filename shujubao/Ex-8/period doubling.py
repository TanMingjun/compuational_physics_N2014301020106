# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:09:41 2016

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
        self.dt=0.01
        self.F_D=F_D
    def calculate(self):
        while self.t[-1]<100:
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
    def plot(self,color):
        py.plot(self.t,self.sita,'b')
        py.xlabel('time [s]')
        py.xlim(0,100)
        py.ylabel('$\\theta$ [radians]')
sub1=py.subplot(221)
A=pendulum0(1.2,0.2)
A.calculate()
sub1.plot(A.t,A.sita,'b',label='$F_D=1.2$')
sub1.set_title('$\\theta$ versus time')
sub1.legend(loc="upper right",frameon=False)
py.ylabel('$\\theta$(radians)')
py.xlabel('time(s)')

sub2=py.subplot(222)
A=pendulum0(1.35,0.2)
A.calculate()
sub2.plot(A.t,A.sita,'b',label='$F_D=1.35$')
sub2.set_title('$\\theta$ versus time')
sub2.legend(loc="upper right",frameon=False)
py.ylabel('$\\theta$(radians)')
py.xlabel('time(s)')

sub3=py.subplot(223)
A=pendulum0(1.44,0.2)
A.calculate()
sub3.plot(A.t,A.sita,'b',label='$F_D=1.44$')
sub3.set_title('$\\theta$ versus time')
sub3.legend(loc="upper right",frameon=False)
py.ylabel('$\\theta$(radians)')
py.xlabel('time(s)')

sub4=py.subplot(224)
A=pendulum0(1.465,0.2)
A.calculate()
sub4.plot(A.t,A.sita,'r',label='$F_D=1.465$')
sub4.set_title('$\\theta$ versus time')
sub4.legend(loc="upper right",frameon=False)
py.ylabel('$\\theta$(radians)')
py.xlabel('time(s)')

py.show()
