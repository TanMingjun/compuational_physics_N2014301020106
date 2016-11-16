# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:04:04 2016

@author: TanMingjun
"""
import matplotlib.pyplot as plt
import numpy as np
class billiard_circle():
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
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
            if (np.sqrt( self.x[i]**2+(self.y[i]-0.01)**2 ) > 1.0) and self.y[i]>0.01:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y-0.01)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect1(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (np.sqrt( self.x[i]**2+(self.y[i]+0.01)**2 ) > 1.0) and self.y[i]<-0.01:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y+0.01)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect2(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (self.x[i] < -1.0) and self.y[i]>-0.01 and self.y[i]<0.01:
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif (self.x[i] > 1.0) and self.y[i]>-0.01 and self.y[i]<0.01:
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            self.t.append(self.t[i - 1] + self.dt)
              
        return self.x, self.y, self.t
        
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt    
    def reflect1(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y-0.01)**2)  ### normalization
        x = x/module
        y = (y-0.01)/module+0.01
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y-0.01))/v
        cos2 = (vx*(y-0.01)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y-0.01)
        vy_n = vt*(y-0.01)-vc*x
        return vx_n,vy_n
    
    def reflect2(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y+0.01)**2)  ### normalization
        x = x/module
        y = (y+0.01)/module-0.01
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y+0.01))/v
        cos2 = (vx*(y+0.01)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y+0.01)
        vy_n = vt*(y+0.01)-vc*x
        return vx_n,vy_n
        
#    def plot(self):
#       plt.figure(figsize = (8,8))
#        plt.xlim(-1,1)
#        plt.ylim(-1,1)
#        plt.xlabel('x')
#       plt.ylabel('y')
#        plt.title('Stadium billiard $\\alpha$=0.01')
#        self.plot_boundary()
#        plt.plot(self.x,self.y,'y')
#        #plt.savefig('chapter3_3.31.png',dpi = 144)
#        plt.show()
                
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

A1=billiard_circle(0,0,1,0.6,4000,0.01)
x1,y1,t1=A1.motion_calculate()
A2=billiard_circle(0.00001,0,1,0.6,4000,0.01)
x2,y2,t2=A2.motion_calculate()
delta=[]
for i in range(len(x1)):
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)
plt.semilogy(t1,x1)
plt.title('Stadium with $\\alpha$=0.01 - divergence of two trajectories')
plt.xlabel('time')
plt.ylabel('separation')


