# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:49:23 2022

@author: SANTANU
"""
'''
t=int(input())
for i in range(t):
    a, b, x=map(int, input().split()) 
    flag=0
    if a>b:
        while a>=b:
            a=a-x
            b=b+x
            if a==b:
               flag=1
    elif b>a:
        while b>=a:
            a=a+x
            b=b-x
            if a==b:
                flag=1
    else:
        flag=1
    if flag==1:
        print('YES')
    else:
        print('NO')
        '''
a, b, x=map(int, input().split())
flag=0
while 0:
    if a>b:
        a=a-x
        b=b+x
        if a==b:
            flag=1
            break
    elif a<b:
        a=a+x
        b=b-x
        if a==b:
            flag=1
            break
    else:
        flag=1
        break
if flag==1:
    print('YES')
else:
    print('NO')































