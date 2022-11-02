# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:11:13 2022

@author: SANTANU
"""
t=int(input())
for i in range(t):
    n=int(input())
    b=list(map(int, input().strip().split()[:n]))
    sum=0
    for j in range(n):
        sum=sum+b[j]
    for k in range(n):
        l=b[k]-(sum/(n+1))
        print(int(l), end=' ')
    print()
   
    