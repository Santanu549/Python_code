# -*- coding: utf-8 -*-

c=0
a=list(map(int,input().strip().split()))
a.sort()
d=[]
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        d.append(a[i])
d.append(a[len(a)-1])
