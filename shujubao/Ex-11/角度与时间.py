# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:32:56 2016

@author: TanMingjun
"""
import pylab as py
import math
class hyperion:
    def __init__(self,theta0,vyc):
        self.gm=4*math.pi**2
        self.xc=[1]
        self.yc=[0]
        self.theta=[theta0]
        self.omega=[0]
        self.vxc=[0]
        self.vyc=[vyc]#这里为了简单起见，将木星比作太阳，小行星比作地球,椭圆与圆由速度决定
        self.dt=0.0001
        self.t=[0]
        
    def run(self):
        while self.t[-1]<=31:
            r=math.sqrt((self.xc[-1])**2+(self.yc[-1])**2)
            vxc_new=self.vxc[-1]-self.gm*self.xc[-1]*self.dt/r**3
            vyc_new=self.vyc[-1]-self.gm*self.yc[-1]*self.dt/r**3
            omega_new=self.omega[-1]-12*(math.pi**2)*(self.xc[-1]*math.sin(self.theta[-1])-self.yc[-1]*math.cos(self.theta[-1]))*(self.xc[-1]*math.cos(self.theta[-1])+self.yc[-1]*math.sin(self.theta[-1]))*self.dt/r**5
    
            self.vxc.append(vxc_new)
            self.vyc.append(vyc_new)
            self.omega.append(omega_new)
    
            self.xc.append(self.xc[-1]+self.vxc[-1]*self.dt)
            self.yc.append(self.yc[-1]+self.vyc[-1]*self.dt)
    
            theta_new=self.theta[-1]+self.omega[-1]*self.dt
            while theta_new > math.pi:
                theta_new -=2*(math.pi)
            while theta_new < -math.pi:
                theta_new +=2*(math.pi)
    
            self.theta.append(theta_new)
            self.t.append(self.t[-1]+self.dt)
        return self.theta,self.t
    def plot(self):
        py.plot(self.t,self.omega,'g')
py.subplot(121)
A=hyperion(0,2*math.pi)
A.run()
A.plot()
py.xlim(0,31)
py.title('Hyperion $\omega$ versus time-Elliptical')
py.xlabel('time(yr)')
py.ylabel('$\omega$(radians/yr)')
py.show

py.subplot(122)
A=hyperion(0,5)
A.run()
A.plot()
py.xlim(0,31)
py.title('Hyperion $\omega$ versus time-Elliptical')
py.xlabel('time(yr)')
py.ylabel('$\omega$(radians/yr)')
py.show