# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:42:45 2016

@author: TanMingjun
"""

from __future__ import division
import numpy as np
from copy import deepcopy
from cmath import *
import matplotlib.pyplot as plt
class power1:
    def __init__(self,a):
        self.a=a
    def iteration(self):
        self.x = np.linspace(0,1,101)
        self.y_now = np.exp(-1000*(self.x-self.a)**2) 
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_before = deepcopy(self.y_now)
        self.y_after = np.zeros(101)
        self.disp = [self.y_now[5]]
        for j in range(2**(10)-1):

            for i in range(101):
                if i== 0 or i== 100:
                    self.y_after[i] = 0
                else:
                    self.y_after[i] = - self.y_before[i] + self.y_now[i+1] + self.y_now[i-1]
 
            self.y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_after)
            self.disp.append(self.y_now[5])
        return self.disp
    def frequency(self):
        self.disp_fft = np.fft.fft(self.disp)
        self.disp_power = []
        self.frequency = []
        for i in range(1024):
            if i==0:
                self.disp_power.append(abs(self.disp_fft[i]))
                f = 0
                self.frequency.append(f)
            else:
                self.disp_power.append(abs(self.disp_fft[i]))
                T = 1024*10**(-4)/(3*i)
                f = 1/T
                self.frequency.append(f)

class power2:
    def __init__(self,a):
        self.a=a
    def iteration(self):
        self.x = np.linspace(0,1,101)
        self.y_now=np.sqrt(0.25-(self.x-0.5+self.a)**2)
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_before = deepcopy(self.y_now)
        self.y_after = np.zeros(101)
        self.disp = [self.y_now[5]]
        for j in range(2**(10)-1):

            for i in range(101):
                if i== 0 or i== 100:
                    self.y_after[i] = 0
                else:
                    self.y_after[i] = - self.y_before[i] + self.y_now[i+1] + self.y_now[i-1]
 
            self.y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_after)
            self.disp.append(self.y_now[5])
        return self.disp
    def frequency(self):
        self.disp_fft = np.fft.fft(self.disp)
        self.disp_power = []
        self.frequency = []
        for i in range(1024):
            if i==0:
                self.disp_power.append(abs(self.disp_fft[i]))
                f = 0
                self.frequency.append(f)
            else:
                self.disp_power.append(abs(self.disp_fft[i]))
                T = 1024*10**(-4)/(3*i)
                f = 1/T
                self.frequency.append(f)
               

class power3:
    def __init__(self,a):
        self.a=a
    def iteration(self):
        self.x = np.linspace(0,1,101)
        self.y_now = np.zeros(101)
        for i in range(101):
            if 40+self.a<=i<=60+self.a:
                self.y_now[i] = 0.5
            else:
                self.y_now[i] = 0
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_before = deepcopy(self.y_now)
        self.y_after = np.zeros(101)
        self.disp = [self.y_now[5]]
        for j in range(2**(10)-1):

            for i in range(101):
                if i== 0 or i== 100:
                    self.y_after[i] = 0
                else:
                    self.y_after[i] = - self.y_before[i] + self.y_now[i+1] + self.y_now[i-1]
 
            self.y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_after)
            self.disp.append(self.y_now[5])
        return self.disp
    def frequency(self):
        self.disp_fft = np.fft.fft(self.disp)
        self.disp_power = []
        self.frequency = []
        for i in range(1024):
            if i==0:
                self.disp_power.append(abs(self.disp_fft[i]))
                f = 0
                self.frequency.append(f)
            else:
                self.disp_power.append(abs(self.disp_fft[i]))
                T = 1024*10**(-4)/(3*i)
                f = 1/T
                self.frequency.append(f)


class power4:
    def __init__(self,a):
        self.a=a
    def iteration(self):
        self.x = np.linspace(0,1,101)
        self.y_now = np.zeros(101)
        for i in range(101):
            if i<=50:
                self.y_now[i] = (1/50)*i-self.a
            else:
                self.y_now[i] = -(1/50)*i + 2 +self.a
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_before = deepcopy(self.y_now)
        self.y_after = np.zeros(101)
        self.disp = [self.y_now[5]]
        for j in range(2**(10)-1):

            for i in range(101):
                if i== 0 or i== 100:
                    self.y_after[i] = 0
                else:
                    self.y_after[i] = - self.y_before[i] + self.y_now[i+1] + self.y_now[i-1]
 
            self.y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_after)
            self.disp.append(self.y_now[5])
        return self.disp
    def frequency(self):
        self.disp_fft = np.fft.fft(self.disp)
        self.disp_power = []
        self.frequency = []
        for i in range(1024):
            if i==0:
                self.disp_power.append(abs(self.disp_fft[i]))
                f = 0
                self.frequency.append(f)
            else:
                self.disp_power.append(abs(self.disp_fft[i]))
                T = 1024*10**(-4)/(3*i)
                f = 1/T
                self.frequency.append(f)

plt.subplot(221)
A1=power1(0.5)
A1.iteration()
A1.frequency()
plt.plot(A1.frequency, A1.disp_power,'k')
A2=power1(0.525)
A2.iteration()
A2.frequency()
plt.plot(A2.frequency, A2.disp_power,'r--')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power(arbitrary units)')
plt.title('Power spectrum-Guass')
plt.xlim(0,3000)
plt.show()

plt.subplot(222)
A1=power2(0)
A1.iteration()
A1.frequency()
plt.plot(A1.frequency, A1.disp_power,'k')
A2=power2(0.01)
A2.iteration()
A2.frequency()
plt.plot(A2.frequency, A2.disp_power,'r--')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power(arbitrary units)')
plt.title('Power spectrum-semicircle')
plt.xlim(0,3000)
plt.show()

plt.subplot(223)
A1=power3(0)
A1.iteration()
A1.frequency()
plt.plot(A1.frequency, A1.disp_power,'k')
A2=power3(0.025)
A2.iteration()
A2.frequency()
plt.plot(A2.frequency, A2.disp_power,'r--')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power(arbitrary units)')
plt.title('Power spectrum-square wave')
plt.xlim(0,3000)
plt.show()

plt.subplot(224)
A1=power4(0)
A1.iteration()
A1.frequency()
plt.plot(A1.frequency, A1.disp_power,'k')
A2=power4(0.05)
A2.iteration()
A2.frequency()
plt.plot(A2.frequency, A2.disp_power,'r--')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power(arbitrary units)')
plt.title('Power spectrum-triangular wave')
plt.xlim(0,3000)
plt.show()