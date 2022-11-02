# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:22:25 2022

@author: SANTANU
"""

def max_min(a, i, j):
    if i==j:
        maxi=mini=a[i]
        return maxi, mini
    elif i==j-1:
        if a[i]>a[j]:
            maxi=a[i]
            mini=a[j]
            return maxi, mini
        else:
            maxi=a[j]
            mini=a[i]
            return maxi, mini
    else:
        mid=(i+j//2)
        maxi, mini=max_min(a, i, mid)
        maxi1,min1=max_min(a, mid+1, j)
        if maxi<maxi1:
            maxi=maxi1
        if mini>min1:
            mini=min1
        return maxi, mini

n=int(input())
a=list(map(int, input().strip().split()))[:n]
maxi, mini=max_min(a, 0, n-1)
print(maxi, mini)
        