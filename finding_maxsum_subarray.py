# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:53:19 2022

@author: SANTANU
"""
def max_min(a, i, j):
    maxi=0
    mini=0
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
        maxi, mini=max_min(a, i, mid)
        r_max, r_min=max_min(a, mid+1, j)
        if maxi<r_max:
            maxi=r_max
        if mini>r_min:
            mini=r_min
        return maxi, mini
n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=[]
sum=0
i=0
while i<n:
    sum=sum+a[i]
    b.append(sum)
    i+=1
ma, mi=max_min(b, 0, n-1)
print(ma)
    