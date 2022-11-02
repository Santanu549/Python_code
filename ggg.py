# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 08:39:56 2022

@author: SANTANU
"""

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if x%3==0:
        a=x/3
        a=int(a)
        b=0
    elif x%3==1:
        a=a+(x/3)+1
        a=int(a)
        b=b+2
    elif x%3==2:
        a=a+(x/3)+1
        a=int(a)
        b=b+1
    if a+b<=n:
        print("Yes")
        print(a,b,n-(a+b))
    else:
        print("No")