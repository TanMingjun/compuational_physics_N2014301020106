# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:30:49 2016

@author: TanMingjun
"""

import math
import pylab as py

# set the mass of sun, jupiter and earth

class three_body_simulation:
     def __init__(self,time, dt=0.001):
         self.gm_sun=4*(math.pi)**2
         self.gm_jupiter=self.gm_sun
         self.gm_earth=self.gm_sun
         self.x_earth=[2]
         self.y_earth=[0]
         self.x_jupiter=[5.2]
         self.y_jupiter=[0]
         self.x_sun=[0]
         self.y_sun=[0]
         self.vx_earth=[0]
         self.vy_earth=[math.sqrt(self.gm_sun/5.2)]
         self.vx_jupiter=[0]
         self.vy_jupiter=[math.sqrt(self.gm_sun/5.2)]
         self.vx_sun=[0]
         self.vy_sun=[-math.sqrt(self.gm_sun/5.2)/1]
         self.dt=dt
         self.t=[0]
         self.time=time
         
     def run(self):
         while self.t[-1]<=self.time:
             r_es=math.sqrt((self.x_earth[-1]-self.x_sun[-1])**2+(self.y_earth[-1]-self.y_sun[-1])**2)
             r_ej=math.sqrt((self.x_earth[-1]-self.x_jupiter[-1])**2+(self.y_earth[-1]-self.y_jupiter[-1])**2)
             r_js=math.sqrt((self.x_jupiter[-1]-self.x_sun[-1])**2+(self.y_jupiter[-1]-self.y_sun[-1])**2)
    
             vx_earth_new=self.vx_earth[-1]-self.gm_sun*(self.x_earth[-1]-self.x_sun[-1])*self.dt/r_es**3-self.gm_jupiter*(self.x_earth[-1]-self.x_jupiter[-1])*self.dt/r_ej**3
             vy_earth_new=self.vy_earth[-1]-self.gm_sun*(self.y_earth[-1]-self.y_sun[-1])*self.dt/r_es**3-self.gm_jupiter*(self.y_earth[-1]-self.y_jupiter[-1])*self.dt/r_ej**3

             vx_jupiter_new=self.vx_jupiter[-1]-self.gm_sun*(self.x_jupiter[-1]-self.x_sun[-1])*self.dt/r_js**3-self.gm_earth*(self.x_jupiter[-1]-self.x_earth[-1])*self.dt/r_ej**3
             vy_jupiter_new=self.vy_jupiter[-1]-self.gm_sun*(self.y_jupiter[-1]-self.y_sun[-1])*self.dt/r_js**3-self.gm_earth*(self.y_jupiter[-1]-self.y_earth[-1])*self.dt/r_ej**3

             vx_sun_new=self.vx_sun[-1]-self.gm_jupiter*(self.x_sun[-1]-self.x_jupiter[-1])*self.dt/r_js**3-self.gm_earth*(self.x_sun[-1]-self.x_earth[-1])*self.dt/r_es**3
             vy_sun_new=self.vy_sun[-1]-self.gm_jupiter*(self.y_sun[-1]-self.y_jupiter[-1])*self.dt/r_js**3-self.gm_earth*(self.y_sun[-1]-self.y_earth[-1])*self.dt/r_es**3

             self.vx_earth.append(vx_earth_new)
             self.vy_earth.append(vy_earth_new)
             self.vx_jupiter.append(vx_jupiter_new)
             self.vy_jupiter.append(vy_jupiter_new)
             self.vx_sun.append(vx_sun_new)
             self.vy_sun.append(vy_sun_new)

             self.x_earth.append(self.x_earth[-1]+self.vx_earth[-1]*self.dt)
             self.y_earth.append(self.y_earth[-1]+self.vy_earth[-1]*self.dt)
             self.x_jupiter.append(self.x_jupiter[-1]+self.vx_jupiter[-1]*self.dt)
             self.y_jupiter.append(self.y_jupiter[-1]+self.vy_jupiter[-1]*self.dt)
             self.x_sun.append(self.x_sun[-1]+self.vx_sun[-1]*self.dt)
             self.y_sun.append(self.y_sun[-1]+self.vy_sun[-1]*self.dt)

             
             self.t.append(self.t[-1]+self.dt)
     def plot(self,color='k',slogan=''):
         py.plot(self.x_earth,self.y_earth,color,label=slogan)
         
     def plot1(self,color='k',slogan=''):
         py.plot(self.x_jupiter,self.y_jupiter,color,label=slogan)
     def plot2(self,color='k',slogan=''):
         py.plot(self.x_sun, self.y_sun,color, label=slogan)
py.subplot(2,2,1)
A1=three_body_simulation(40)
A1.run()
A1.plot(color='r',slogan=r'earth')
A1.plot1(color='g',slogan=r'jupiter')
A1.plot2(color='b',slogan=r'sun')
py.xlim(-15,15)
py.ylim(0,30)
py.legend(loc='upper right')
py.title('Mass of jupiter=earth=sun')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,2)
A2=three_body_simulation(40)
A2.run()
A2.plot(color='r',slogan=r'earth')
py.xlim(-15,15)
py.ylim(0,30)
py.legend(loc='upper right')
py.title('Mass of jupiter=earth=sun')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,3)
A3=three_body_simulation(40)
A3.run()
A3.plot1(color='g',slogan=r'jupiter')
py.xlim(-15,15)
py.ylim(0,30)
py.legend(loc='upper right')
py.title('Mass of jupiter=earth=sun')
py.xlabel('x(AU)')
py.ylabel('y(AU)')

py.subplot(2,2,4)
A4=three_body_simulation(40)
A4.run()
A4.plot2(color='b',slogan=r'sun')
py.xlim(-15,15)
py.ylim(0,30)
py.legend(loc='upper right')
py.title('Mass of jupiter=earth=sun')
py.xlabel('x(AU)')
py.ylabel('y(AU)')
py.show()
