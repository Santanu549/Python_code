# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:22:02 2022

@author: SANTANU
"""

n=int(input())
a=list(map(int,input().strip().split()))[:n]
r=int(input())
temp=0
for j in range(r):
    temp=a[n-1]
    for i in range(n-1):
        a[n-1-i]=a[n-2-i]
    a[0]=temp

