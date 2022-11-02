# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:14:51 2022

@author: SANTANU
"""

t=int(input())
for i in range(t):
    a=list(map(int, input().strip().split()[:6]))
    l=0
    m=0
    f=0
    g=0
    for j in range(2):
        if a[2*j]==1 and a[2*j+1]==2:
            l=l+1
        elif a[2*j]==2 and a[2*j+1]==1:
            f=f+1
        elif a[2*j]==3 and a[2*j+1]==4:
            m=m+1
        elif a[2*j]==4 and a[2*j+1]==3:
            g=g+1
    print(l+f,m+g)
    if l+f>m+g:
        print(1)
    elif m+g>l+f:
        print(2)
    else:
        print(0)