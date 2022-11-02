# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 01:52:29 2022

@author: SANTANU
"""

def min_SEC_min(a, i, j):
    maxi=0
    mini=0
    mini_a=0
    if i==j:
        maxi=mini=a[i]
        return maxi, mini
    elif i==j-1:
        if a[i]<a[j]:
            maxi=a[j]
            mini = a[i]
            return maxi, mini
        else:
            maxi=a[i]
            mini=a[j]
            return maxi, mini
    else:
        mid=int(i+j/2)
        maxi, mini=min_SEC_min(a, i, mid)
        r_max, r_min=min_SEC_min(a, mid+1, j)
        if mini>r_min:
            mini_a=r_min
            if mini>r_max:
                maxi=r_max
            else:
                maxi=mini
        else:
            mini_a=mini
            if r_min<maxi:
                maxi=r_min
        return maxi, mini_a
n=int(input())
a=list(map(int,input().strip().split()))[:n]
ma, mi=min_SEC_min(a, 0, n-1)
print(ma, mi)