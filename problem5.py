# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 13:31:11 2021

@author: Nathan Maupin
"""
import pandas as pd

h = 5
t = [0, 5, 10, 15, 20, 25]
T = [80, 44.5, 30, 24.1, 21.7, 20.7]
g = []


def forward1(T1, T2, T3):
    return (1/(2*h))*(-3*T1 + 4*T2 - T3)

def center1(T1, T2):
    return (1/(2*h))*(T1 - T2)

def backward1(T1,T2, T3):
    return (1/(2*h))*(T1 - 4*T2 + 3*T3)

for i, j in enumerate(T):
    check = False
    
    if i >= 1 and i <= 4 and check == False:
        check = True
        g.append(center1(T[i+1], T[i-1]))
    if i <= 3 and check == False:
        check = True
        g.append(forward1(T[i], T[i+1], T[i+2]))
    if i >= 2 and check == False:
        check = True
        g.append(backward1(T[i-2], T[i-1], T[i])
                        )
setup = {"Time (sec)":[t[0], t[1], t[2], t[3], t[4], t[5]], 
         "Gradient": [g[0], g[1], g[2], g[3], g[4], g[5]]}
grad_table = pd.DataFrame(setup, columns = ['Time (sec)', 'Gradient'])
print(grad_table)

