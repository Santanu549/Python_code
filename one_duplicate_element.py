# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 02:10:12 2022

@author: SANTANU
"""

def minJumps(arr, n):
        i=0
        c=0
        while i<n-1:
            i=i+arr[i]
            c+=1
        return c
n=int(input())
arr=list(map(int,input().strip().split()))[:n]
ans=minJumps(arr, n)