# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:36:32 2022

@author: SANTANU
"""

from array import *
n=int(input())
arr=array('i',[])
for i in range(n-1):
    x=int(input())
    arr.append(x)
print(arr)
arr.insert(3, 6)
print(arr)