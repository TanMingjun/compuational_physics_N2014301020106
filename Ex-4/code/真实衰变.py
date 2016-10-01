# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:21:02 2016

@author: TanMingjun
"""
import math
import pylab as py
NA_0=float(input('The initial number of A: '))
NB_0=float(input('The initial number of B: '))
t_0=float(input('The initial number of time: '))
dt=float(input('The time step is: '))
NA=[NA_0]
NB=[NB_0]
t=[t_0]

for i in range(1000):
    y_NA=50+50*(math.e)**(-2*t[i])
    y_NB=50-50*(math.e)**(-2*t[i])
    t_next=t[i]+dt
    NA.append(y_NA)
    NB.append(y_NB)
    t.append(t_next)

py.plot(t,NA,'c')
py.plot(t,NB,'y')
py.xlabel('time ($s$)')
py.ylabel('Number of Nuclei')
py.legend(loc="upper right", frameon=False)
py.show()