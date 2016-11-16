# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:58:16 2016

@author: TanMingjun
"""

import matplotlib.pyplot as plt
import numpy as np
class billiard_circle():
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt,alpha):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
        self.alpha=alpha
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (np.sqrt( self.x[i]**2+(self.y[i]-self.alpha)**2 ) > 1.0) and self.y[i]>self.alpha:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y-self.alpha)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect1(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (np.sqrt( self.x[i]**2+(self.y[i]+self.alpha)**2 ) > 1.0) and self.y[i]<-self.alpha:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y+self.alpha)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect2(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (self.x[i] < -1.0) and self.y[i]>-self.alpha and self.y[i]<self.alpha:
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif (self.x[i] > 1.0) and self.y[i]>-self.alpha and self.y[i]<self.alpha:
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            self.t.append(self.t[i - 1] + self.dt)
              
        return self.x, self.y
        
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt    
    def reflect1(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y-self.alpha)**2)  ### normalization
        x = x/module
        y = (y-self.alpha)/module+self.alpha
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y-self.alpha))/v
        cos2 = (vx*(y-self.alpha)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y-self.alpha)
        vy_n = vt*(y-self.alpha)-vc*x
        return vx_n,vy_n
    
    def reflect2(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y+self.alpha)**2)  ### normalization
        x = x/module
        y = (y+self.alpha)/module-self.alpha
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y+self.alpha))/v
        cos2 = (vx*(y+self.alpha)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y+self.alpha)
        vy_n = vt*(y+self.alpha)-vc*x
        return vx_n,vy_n
        
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Stadium billiard $\\alpha$=0.01')
        self.plot_boundary()
        plt.plot(self.x,self.y,'y')
        #plt.savefig('chapter3_3.31.png',dpi = 144)
        plt.show()
                
#    def plot_boundary(self):
#        theta = 0
#        x = []
#        y = []
#        while theta < np.pi:
#            x.append(np.cos(theta))
#            y.append(np.sin(theta)+0.01)
#            theta+= 0.01
#        plt.plot(x,y,'g.')
#        while theta > np.pi and theta< 2*np.pi:
#            x.append(np.cos(theta))
#            y.append(np.sin(theta)-0.01)
#            theta+= 0.01
#        plt.plot(x,y,'g.')
    def phase_plot(self):
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        return record_vx, record_x
#        plt.xlabel('x')
#        plt.ylabel(r'$v_x$')
#        plt.scatter(record_x,record_vx,s=1)
        #plt.savefig('chapter3_3.31_phasey=0.png', dpi= 144)
#        plt.show()
sub1=plt.subplot(221)
A=billiard_circle(0.2,0,1,0.6,500000,0.01,0)
A.motion_calculate()
vx,x=A.phase_plot()
sub1.scatter(x, vx,s=1)
plt.xlabel('x')
plt.ylabel('$v_x$')
sub1.set_title('$\\alpha=0$')
plt.show()

sub2=plt.subplot(222)
A=billiard_circle(0.2,0,1,0.6,500000,0.01,0.001)
A.motion_calculate()
vx,x=A.phase_plot()
sub2.scatter(x, vx,s=1)
plt.xlabel('x')
plt.ylabel('$v_x$')
sub2.set_title('$\\alpha=0.001$')
plt.show()

sub3=plt.subplot(223)
A=billiard_circle(0.2,0,1,0.6,500000,0.01,0.01)
A.motion_calculate()
vx,x=A.phase_plot()
sub3.scatter(x, vx,s=1)
plt.xlabel('x')
plt.ylabel('$v_x$')
sub3.set_title('$\\alpha=0.01$')
plt.show()

sub4=plt.subplot(224)
A=billiard_circle(0.2,0,1,0.6,500000,0.01,0.1)
A.motion_calculate()
vx,x=A.phase_plot()
sub4.scatter(x, vx,s=1)
plt.xlabel('x')
plt.ylabel('$v_x$')
sub4.set_title('$\\alpha=0.1$')
plt.show()