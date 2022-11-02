# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:10:58 2022

@author: SANTANU
"""

from array import *
n=int(input('enter the elements number you want: '))
arr=array('i',[])
for i in range(n):
    x=int(input('enter element: '))
    arr.append(x)
print(arr)
val=int(input('enter the elememt you want to search: '))
l=0
for i in range(n):
    if arr[i]==val:
        l=1
        count=i+1
        break
if l==0:
    print('not found')
else:
    print('found at index {}'.format(count))