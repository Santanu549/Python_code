# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:16:14 2022

@author: SANTANU
"""


n,x=map(int,input().split())
for i in range(0,n+1):
    for j in range(0,n-i+1):
        if 3*i-j==x:
            a=i
            b=j
            l=1
        else:
            l=0 
            a=0
            b=0
c=n-a-b
if l==1:
    
    print("Yes")
    print(a,b,c)
else:
    print("No")