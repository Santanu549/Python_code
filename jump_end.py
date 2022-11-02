# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 01:39:51 2022

@author: SANTANU
"""

n=int(input())
a=list(map(int,input().strip().split()))[:n]
i=0
c=0
while i<n-1:
    i=i+a[i]
    c+=1