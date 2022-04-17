#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:01:28 2022

@author: sangyoon
"""

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

nList.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 
        
        if array[mid] == target:
            print("yes", end=" ")
            return 
        elif array[mid] > target: 
            end = mid - 1
        else:
            start = mid + 1
    print("no", end=" ")

for item in mList:
    binary_search(nList, item, 0, len(nList) - 1)
    