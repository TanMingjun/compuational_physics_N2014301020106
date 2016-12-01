# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:14:57 2016

@author: TanMingjun
"""

import math
import pylab as py

# set the mass of sun, jupiter and earth

class three_body_simulation:
     def __init__(self,time,pei, dt=0.00001):
         self.pei=pei
         self.gm_sun=4*(math.pi)**2
         self.gm_jupiter=(317*self.pei/330000)*self.gm_sun
         self.gm_earth=self.gm_sun*(1/330000)
         self.x_earth=[1]
         self.y_earth=[0]
         self.x_jupiter=[5.2]
         self.y_jupiter=[0]
         self.vx_earth=[0]
         self.vy_earth=[2*math.pi]
         self.vx_jupiter=[0]
         self.vy_jupiter=[math.sqrt(self.gm_sun/5.2)]
         self.dt=dt
         self.t=[0]
         self.time=time
        
     def run(self):
         while self.t[-1]<=self.time:
             r_es=math.sqrt((self.x_earth[-1])**2+(self.y_earth[-1])**2)
             r_ej=math.sqrt((self.x_earth[-1]-self.x_jupiter[-1])**2+(self.y_earth[-1]-self.y_jupiter[-1])**2)
             r_js=math.sqrt((self.x_jupiter[-1])**2+(self.y_jupiter[-1])**2)
    
             vx_earth_new=self.vx_earth[-1]-self.gm_sun*(self.x_earth[-1])*self.dt/r_es**3-self.gm_jupiter*(self.x_earth[-1]-self.x_jupiter[-1])*self.dt/r_ej**3
             vy_earth_new=self.vy_earth[-1]-self.gm_sun*(self.y_earth[-1])*self.dt/r_es**3-self.gm_jupiter*(self.y_earth[-1]-self.y_jupiter[-1])*self.dt/r_ej**3

             vx_jupiter_new=self.vx_jupiter[-1]-self.gm_sun*(self.x_jupiter[-1])*self.dt/r_js**3-self.gm_earth*(self.x_jupiter[-1]-self.x_earth[-1])*self.dt/r_ej**3
             vy_jupiter_new=self.vy_jupiter[-1]-self.gm_sun*(self.y_jupiter[-1])*self.dt/r_js**3-self.gm_earth*(self.y_jupiter[-1]-self.y_earth[-1])*self.dt/r_ej**3

             self.vx_earth.append(vx_earth_new)
             self.vy_earth.append(vy_earth_new)
             self.vx_jupiter.append(vx_jupiter_new)
             self.vy_jupiter.append(vy_jupiter_new)

             self.x_earth.append(self.x_earth[-1]+self.vx_earth[-1]*self.dt)
             self.y_earth.append(self.y_earth[-1]+self.vy_earth[-1]*self.dt)
             self.x_jupiter.append(self.x_jupiter[-1]+self.vx_jupiter[-1]*self.dt)
             self.y_jupiter.append(self.y_jupiter[-1]+self.vy_jupiter[-1]*self.dt)

             self.t.append(self.t[-1]+self.dt)
     def plot(self,color='k',slogan=''):
         py.plot(self.x_earth,self.y_earth,color,label=slogan)
         
     def plot1(self,color='k',slogan=''):
         py.plot(self.x_jupiter,self.y_jupiter,color,label=slogan)
py.subplot(2,2,1)
A1=three_body_simulation(5,1)
A1.run()
A1.plot(color='r',slogan=r'earth')
A1.plot1(color='g',slogan=r'jupiter')
py.scatter(0,0,color="yellow",s=50,label='sun')
py.xlim(-6,6)
py.ylim(-6,6)
py.legend(loc='upper right')
py.title('Mass of jupiter=1Mj')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,2)
A2=three_body_simulation(5,10)
A2.run()
A2.plot(color='r',slogan=r'earth')
A2.plot1(color='g',slogan=r'jupiter')
py.scatter(0,0,color="yellow",s=50,label='sun')
py.xlim(-6,6)
py.ylim(-6,6)
py.legend(loc='upper right')
py.title('Mass of jupiter=10Mj')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,3)
A3=three_body_simulation(5,100)
A3.run()
A3.plot(color='r',slogan=r'earth')
A3.plot1(color='g',slogan=r'jupiter')
py.scatter(0,0,color="yellow",s=50,label='sun')
py.xlim(-6,6)
py.ylim(-6,6)
py.legend(loc='upper right')
py.title('Mass of jupiter=100Mj')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,4)
A4=three_body_simulation(5,1000)
A4.run()
A4.plot(color='r',slogan=r'earth')
A4.plot1(color='g',slogan=r'jupiter')
py.scatter(0,0,color="yellow",s=50,label='sun')
py.xlim(-6,6)
py.ylim(-6,6)
py.legend(loc='upper right')
py.title('Mass of jupiter=1000Mj')
py.xlabel('x(AU)')
py.ylabel('y(AU)')
py.show()

