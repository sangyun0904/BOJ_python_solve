#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:50:46 2022

@author: sangyoon
"""

n, m = list(map(int, input().split()))

trees = list(map(int, input().split()))
trees.sort()

def binary_search(trees, target):
    start = 0 
    end = trees[n - 1]
    while True :
        mid = (start + end) // 2
        result = 0 
        for tree in trees:
            if tree > mid:     
                result += tree - mid
        if result == target :
            return mid
        elif result > target:
            start = mid + 1
            if start > end:
                return mid
        else:
            end = mid - 1 
            if start > end:
                return mid - 1

print(binary_search(trees, m))