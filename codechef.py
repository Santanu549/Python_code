# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:19:45 2022

@author: SANTANU
"""
q=0
x=int(input())
for i in range(x):
    for j in range(x):
        for k in range(x):
             if (i^j)+(j^k)+(k^i)==x:
                q=1
                a=i
                b=j
                c=k
                break
if q==1:
   print(a,b,c,)
else:
    print(-1)
                