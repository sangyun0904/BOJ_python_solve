#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:27:25 2022

@author: sangyoon
"""

N = int(input())
array = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
array.sort()
print(array)

def binary_search(array, target):
    start = 0 
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1 
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0 

for i in targets:
    print(binary_search(array, i))
    
        