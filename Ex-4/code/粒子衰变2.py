# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:32:35 2016

@author: TanMingjun
"""
import pylab as py
NA_0=float(input('The initial number of A: '))
NB_0=float(input('The initial number of B: '))
t_0=float(input('The initial number of time: '))
dt=float(input('The time step is: '))
NA=[NA_0]
NB=[NB_0]
t=[t_0]

for i in range(200):
    NA_n=NA[i]+(NB[i]-NA[i])*dt
    NB_n=NB[i]+(NA[i]-NB[i])*dt
    t_next=t[i]+dt
    NA.append(NA_n)
    NB.append(NB_n)
    t.append(t_next)

py.plot(t,NA,'b')
py.plot(t,NB,'r')
py.xlabel('time ($s$)')
py.ylabel('Number of Nuclei')
py.xlim(min(t),max(t))
py.xticks([0,1,2,3,4,5,6,7,8,9,10])
py.yticks([0,20,40,60,80,100])
py.legend(loc="upper right", frameon=False)
py.show()


