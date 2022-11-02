# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 07:39:32 2022

@author: SANTANU
"""

T=int(input())
for i in range(T):
    n,x=map(int,input().split())
    if x==0:
        for j in range(1,n):
            for k in range(1,n-j):
                if (3*j-k)==0:
                    a=j
                    a=int(a)
                    b=k
                    b=int(b)
        print("Yes")
        print(a,b)        
    else:  
        if x%3==0:
            a=x/3
            a=int(a)
            b=0
            if a+b<=n:
                print('Yes')
                print(a,0,n-a)
            else:
                print('No')
        elif x%3==1:
            a=(x/3)+1
            a=int(a)
            b=2
            if a+b<=n:
                print('Yes')
                print(a,2,n-2-a)
            else:
                print('No')
        elif x%3==2:
            a=(x/3)+1
            a=int(a)
            b=1
            if a+b<=n:
                print('Yes')
                print(a,1,n-1-a)
            else:
                print('No')
        else:
            print("No")