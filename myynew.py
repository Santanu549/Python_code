# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:40:46 2022

@author: SANTANU
"""

def minimum(x):
    mini = x[0]
    for i in x:
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
print(minimum(a))
#faiyaz ullah is here ,friend ofnsantanu