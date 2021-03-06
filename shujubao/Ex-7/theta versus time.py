# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:51:46 2016

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
        while self.t[-1]<60:
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
        py.ylabel('$\theta$ [radians]')
sub1=py.subplot(231)
A=pendulum0(0,0.2)
A.calculate()
sub1.plot(A.t,A.sita,'b',label='$F_D=0$')
sub1.set_title('$theta$ versus time')
sub1.legend(loc="upper right",frameon=False)
py.ylabel('theta(radians)')
py.xlabel('time(s)')

sub2=py.subplot(232)
A=pendulum0(0.5,0.2)
A.calculate()
sub2.plot(A.t,A.sita,'b',label='$F_D=0.5$')
sub2.set_title('$theta$ versus time')
sub2.legend(loc="upper right",frameon=False)
py.ylabel('theta(radians)')
py.xlabel('time(s)')

sub3=py.subplot(233)
A=pendulum0(1.2,0.2)
A.calculate()
sub3.plot(A.t,A.sita,'b',label='$F_D=1.2$')
sub3.set_title('$theta$ versus time')
sub3.legend(loc="upper right",frameon=False)
py.ylabel('theta(radians)')
py.xlabel('time(s)')

sub4=py.subplot(234)
A=pendulum0(0,0.2)
A.calculate()
sub4.plot(A.t,A.omiga,'r',label='$F_D=0$')
sub4.set_title('$w$ versus time')
sub4.legend(loc="upper right",frameon=False)
py.ylabel('$w$(radians/s)')
py.xlabel('time(s)')

sub5=py.subplot(235)
A=pendulum0(0.5,0.2)
A.calculate()
sub5.plot(A.t,A.omiga,'r',label='$F_D=0.5$')
sub5.set_title('$w$ versus time')
sub5.legend(loc="upper right",frameon=False)
py.ylabel('$w$(radians/s)')
py.xlabel('time(s)')

sub6=py.subplot(236)
A=pendulum0(1.2,0.2)
A.calculate()
sub6.plot(A.t,A.omiga,'r',label='$F_D=1.2$')
sub6.set_title('$w$ versus time')
sub6.legend(loc="upper right",frameon=False)
py.ylabel('$w$(radians/s)')
py.xlabel('time(s)')


py.show()


    