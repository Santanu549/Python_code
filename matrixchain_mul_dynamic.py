# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 03:24:22 2022

@author: SANTANU
"""
import sys
def mm(a, n):
    dp=[[0 for i in range(100)] for j in range(100)]
    for le in range(2,n):
        col=le
        for row in range(0,n-le):
            dp[row][col]=sys.maxsize
            for k in range(row+1,col):
                dp[row][col]=min(dp[row][col], dp[row][k]+dp[k][col]+a[row]*a[k]*a[col])
            col=col+1
    return dp[0][n-1]
a=[40, 20, 30, 10, 30]
n=len(a)
print(mm(a, n))
            
    