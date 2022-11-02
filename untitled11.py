# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 00:17:47 2022

@author: SANTANU
"""
ans=0
a=[1,2,3,4,3]
for i in range(len(a)):
        ans=ans^a[i]
for j in range(len(a)-1):
    ans=ans^a[j]