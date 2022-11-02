# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 19:07:58 2022

@author: SANTANU
"""
"""
n=int(input())
a=list(map(int, input().strip().split()))[:n]
sum=0
for i in range(len(a)):
    sum=sum^a[i]
    for j in range(len(a)-1):
        sum=sum^a[j]
print(sum)
"""
n=int(input())
a=list(map(int, input().strip().split()))[:n]
a.sort()
b=[]
c=[]
count=1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count=count+1
    else:
        c.append(i)
        i+=1
        b.append(count)
        count=1