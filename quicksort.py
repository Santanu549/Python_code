# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:31:19 2022

@author: SANTANU
"""

def partition(a, lb, ub):
    i=lb
    j=ub
    pivot=a[lb]
    while i<j:
        while a[i]<=pivot:
            i=i+1
        while a[j]>pivot:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[lb],a[j]=a[j],a[lb]
    return j
def q_short(a, lb, ub):
    if lb<ub:
        loc = partition(a, lb, ub)
        q_short(a, lb, loc-1)
        q_short(a, loc+1, ub)
    return a
n=int(input())
a=list(map(int, input().strip().split()))[:n]
q_short(a, 0, n-1)
'''
def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high]
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):
   if low < high:
      pi = partition(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)
n=int(input())
arr=list(map(int, input().strip().split()))[:n]
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
   print (arr[i],end=" ")
   '''