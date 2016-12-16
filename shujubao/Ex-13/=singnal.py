# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:13:08 2016

@author: TanMingjun
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

class waves1:
    def _init_(self):
        
        self.x = np.linspace(0,1,101)
        self.y = np.exp(-1000*(self.x-0.3)**2)+0.5*np.exp(-1000*(self.x-0.7)**2)
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,1,101)

        self.y_now = np.exp(-1000*(self.x-0.3)**2)+0.5*np.exp(-1000*(self.x-0.7)**2) 
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1200):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append(self.y_now[5])
            self.T.append(0.01/300*j)
           
                
        return self.y_now, self.T,self.N

class waves2:
    def _init_(self):
        
        self.x = np.linspace(0,1,101)
        self.y = np.sqrt(0.25-(self.x-0.5)**2)
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,1,101)

        self.y_now = np.sqrt(0.25-(self.x-0.5)**2)
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1200):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append(self.y_now[5])
            self.T.append(0.01/300*j)
           
                
        return self.y_now, self.T,self.N

class waves3:
    def _init_(self):
        
        self.x = np.linspace(0,1,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 10<=i<=30:
                self.y[i] = 0.5
            else:
                self.y[i] = 0
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,1,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 10<=i<=30:
                self.y_now[i] = 0.5
            else:
                self.y_now[i] = 0
        self.y_now = np.exp(-1000*(self.x-0.3)**2) 
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1200):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append(self.y_now[5])
            self.T.append(0.01/300*j)
           
                
        return self.y_now, self.T,self.N

class waves4:
    def _init_(self):
        
        self.x = np.linspace(0,1,101)
        self.y= np.zeros(101)
        for i in range(101):
            if 0<=i<=25:
                self.y[i] = 1/50*i
            else:
                self.y[i] = -1/150*i+2/3
        self.y[0] = 0
        self.y[-1] = 0

    def iteration(self):

        self.x = np.linspace(0,1,101)
        self.y_now= np.zeros(101)
        for i in range(101):
            if 0<=i<=25:
                self.y_now[i] = 1/50*i
            else:
                self.y_now[i] = -1/150*i+2/3
        self.y_now[0] = 0
        self.y_now[-1] = 0

        self.y_old = deepcopy(self.y_now)
        self.y_new = np.zeros(101)
        self.T=[]
        self.N=[]
        for j in range(1200):
            for i in range(101):
                if i== 0 or i== 100:
                    self.y_new[i] = 0
                else:
                    self.y_new[i] = - self.y_old[i] + self.y_now[i+1] + self.y_now[i-1]
            self.y_old = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_new)
            self.N.append(self.y_now[5])
            self.T.append(0.01/300*j)
           
                
        return self.y_now, self.T,self.N

plt.subplot(221)
A = waves1()
A.iteration()
plt.plot(A.T,A.N,'r')
plt.xlabel('Time(s)')
plt.ylabel('Signal(arbitrary units)')
plt.title('two Gauss')
plt.grid(True)
plt.show()

plt.subplot(222)
A = waves2()
A.iteration()
plt.plot(A.T,A.N,'g')
plt.xlabel('Time(s)')
plt.ylabel('Signal(arbitrary units)')
plt.title('Semicircle')
plt.grid(True)
plt.show()

plt.subplot(223)
A = waves3()
A.iteration()
plt.plot(A.T,A.N,'k')
plt.xlabel('Time(s)')
plt.ylabel('Signal(arbitrary units)')
plt.title('Square wave')
plt.grid(True)
plt.show()

plt.subplot(224)
A = waves4()
A.iteration()
plt.plot(A.T,A.N,'b')
plt.xlabel('Time(s)')
plt.ylabel('Signal(arbitrary units)')
plt.title('Triangular wave')
plt.grid(True)
plt.show()