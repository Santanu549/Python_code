# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:56:28 2022

@author: SANTANU
"""

def fibbo(n):
    f=[0]*(n+1)
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]


n=int(input())
res=fibbo(n)