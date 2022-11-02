# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:26:04 2022

@author: SANTANU
"""
d=0
l=4
r=0
u=0
do=4
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for j in range(16):
    if d==0:
        for i in range(l):
            print(a[r][i])
        u=u+1
    elif d==1:
        for i in range(u,do):
            print(a[i][l])
        l=l-1
    elif d==2:
        for i in range(l,r):
            print(a[i][do])
        do=do-1
    elif d==3:
        for i in range(do,u):
            print(a[r][i])
        r=r+1
    d=(d+1)%4
    
            