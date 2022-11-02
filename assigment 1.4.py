# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:04:25 2022

@author: SANTANU
"""

a=[]
n=int(input("enter the elements number you want in the list: "))
for i in range(n):
    b=int(input("element = "))
    a.append(b)
print("the minimum number of the list is", min(a))