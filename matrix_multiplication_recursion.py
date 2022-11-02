# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 03:02:50 2022

@author: SANTANU
"""
import sys

def matrix_mul_recursion(a, i, j):
    if i>=j:
        return 0
    res = sys.maxsize
    temp=0
    for k in range(i,j):
        temp = matrix_mul_recursion(a, i, k)+matrix_mul_recursion(a, k+1, j)+a[i-1]*a[k]*a[j]
        if temp<res:
            res=temp
    return res

a=[40, 20, 30, 10, 30]
res=matrix_mul_recursion(a, 1, len(a)-1)