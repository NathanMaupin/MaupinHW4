# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:03:07 2021

@author: Nathan Maupin

"""

# 1.  Numerical Differentiation (20 pts) Code.

import numpy as np
import math
import matplotlib.pyplot as plt


h = 1e-8
f_array = []
E = []
N = np.arange(0, 4, 0.04)

def f(x): 
    return math.sin(x)

def fprime(x):
    return math.cos(x)

def fiveend(x):
    return 1/(12*h)*(-25*f(x) + 48*f((x+h)) - 36*f(x+2*h) + 16*f(x+3*h) - 3*f(x+4*h)) 

def fivemid(x):
    return 1/(12*h)*(f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))   


for count, n in enumerate(N):
    # if statements check for which 5-point has less absolute error
    if abs(fprime(n)-fivemid(n)) < abs(fprime(n)-fiveend(n)):
        print("exact:", n, fprime(n))
        print("five-mid:",n, fivemid(n))
        print("E",abs(fprime(n)-fivemid(n)))
        E.append(abs(fprime(n)-fivemid(n)))
    else:
        print("exact:", n, fprime(n))
        print("five-end:",n, fiveend(n))
        E.append(abs(fprime(n)-fiveend(n)))
        
plt.plot(N, E)
plt.show()
