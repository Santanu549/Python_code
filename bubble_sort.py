# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 01:55:49 2022

@author: SANTANU
"""

a=[0,1,2]
b=[5,15,10]
for i in range(1,len(a)):
    for j in range(1,len(a)-i):
        if b[j]>b[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            b[j],b[j+1]=b[j+1],b[j]
s=[]
sum=0
for i in range(0,len(a)):
    s.append(sum)
    sum=sum+b[i]
s.append(sum)
wt=[]
for i in range(0,len(a)):
    wt.append(s[i]-a[i])
