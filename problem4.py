# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 13:30:57 2021

@author: Nathan Maupin
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


h = math.pi/8
E_forward = []
E_center = []
E_backward = []


# Part a
def f(x):
    return x + math.sin(x)

def fprime(x):
    return -1*math.sin(x)

def backward32(x):
    return 1/h**2*(f(x-2*h) - 2*f(x-h) + f(x))

def center32(x):
    return 1/h**2*(f(x-h) - 2*f(x) + f(x+h))

def forward32(x):
    return 1/h**2*(f(x) - 2*f(x+h) + f(x+2*h))

setup = {"derivative": ["f'' exact", "f'' forward", "f'' centered", "f'' backward"],
         "values": [str(fprime(1)), str(forward32(1)), str(center32(1)), 
                    backward32(1)]}
table = pd.DataFrame(setup, columns = ['derivative', 'values'])
print(table)

# Part b
N = np.arange(-0.5, 0.5, 0.001)
print(len(N))
for count, n in enumerate(N):
    E_forward.append(abs(fprime(n)-forward32(n)))
    E_center.append(abs(fprime(n)-center32(n)))
    E_backward.append(abs(fprime(n)-backward32(n)))
   
plt.plot(N, E_forward, label="Forward")
plt.plot(N, E_center, label="Center")
plt.plot(N, E_backward, label="backward")
plt.legend()
plt.show()
