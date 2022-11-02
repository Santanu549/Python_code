# -*- coding: utf-8 -*-
"""
Created on Tue May 24 01:18:19 2022

@author: SANTANU
"""

def mini(a):
    mi=a[0]
    for i in range(n):
        if a[i]<mi:
            mi=a[i]
    print('the minimum is : ',mi)
def maxi(a):
    ma=a[0];
    for i in range(n):
        if a[i]>ma:
            ma=a[i]
    print('the maximum is : ',ma)
    
n=int(input())
a=list(map(int, input().strip().split()))[:n]
mini(a)
maxi(a)