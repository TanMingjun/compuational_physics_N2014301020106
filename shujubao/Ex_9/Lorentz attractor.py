# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:32:43 2016

@author: TanMingjun
"""
import pylab as py
class phase_space:
    def __init__(self,r):
        self.x=[1]
        self.y=[0]
        self.z=[0]
        self.vx=[0]
        self.vy=[0]
        self.vz=[0]
        self.t=[0]
        self.dt=0.0001
        self.sigma=10
        self.b=8/3
        self.r=r
        self.xn=[]
        self.yn=[]
        self.zn=[]
    def calculate1(self):
        for i in range(5000000):
            self.vx.append(self.sigma*(self.y[-1]-self.x[-1]))
            self.vy.append(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
            self.vz.append(self.x[-1]*self.y[-1]-self.b*self.z[-1])
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.z.append(self.z[-1]+self.vz[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            if self.t[-1]>30:
                if abs(self.x[-1])<0.01:
                    self.yn.append(self.y[-1])
                    self.zn.append(self.z[-1])
        return self.yn,self.zn
    def calculate2(self):
        for i in range(5000000):
            self.vx.append(self.sigma*(self.y[-1]-self.x[-1]))
            self.vy.append(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
            self.vz.append(self.x[-1]*self.y[-1]-self.b*self.z[-1])
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.z.append(self.z[-1]+self.vz[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            if self.t[-1]>30:
                if abs(self.y[-1])<0.01:
                    self.xn.append(self.x[-1])
                    self.zn.append(self.z[-1])
        return self.yn,self.xn
sub1=py.subplot(211)
A=phase_space(25)
A.calculate1()
sub1.plot(A.yn,A.zn,'k.')
sub1.set_title('When x=0')
py.xlabel('y')
py.ylabel('z')

sub2=py.subplot(212)
A=phase_space(25)
A.calculate2()
sub2.plot(A.xn,A.zn,'k.')
sub1.set_title('When y=0')
py.xlabel('x')
py.ylabel('z')