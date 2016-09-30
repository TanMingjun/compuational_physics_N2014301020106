# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:30:56 2016

@author: TanMingjun
"""

import pylab as py
class exchangable_decay:
    def __init__(self, number_A = 100, number_B=0, time_constant = 1, time_of_duration = 6, time_step = 0.05):
        # unit of time is second
        self.n_A = [number_A]
        self.n_B = [number_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
    def calculate(self):
         for i in range(self.nsteps):
            tmp_01 = self.n_A[i] + (self.n_B[i]/self.tau- self.n_A[i] / self.tau) * self.dt
            tmp_02 = self.n_B[i] + (self.n_A[i]/self.tau- self.n_B[i] / self.tau) * self.dt
            self.n_A.append(tmp_01)
            self.n_B.append(tmp_02)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        py.plot(self.t, self.n_A)
        py.plot(self.t, self.n_B,'r')
        py.xlabel('time ($s$)')
        py.ylabel('Number of Nuclei')
        py.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_A[i], self.n_B[i], file = myfile)
        myfile.close()
a = exchangable_decay()
a.calculate()
a.show_results()
a.store_results()