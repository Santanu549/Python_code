# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 01:42:39 2022

@author: SANTANU
"""

def minimum(x):
    mini = x[0]
    for i in x[0: ]:
        if i < mini:
            mini = i
        else:
            mini = x[0]
    return (mini)

a=[]
n=int(input("enter the elements number you want in the list: "))
for i in range(n):
    b=int(input("element = "))
    a.append(b)
print("the minimum number is", minimum(a))