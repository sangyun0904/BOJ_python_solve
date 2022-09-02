#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:46:02 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

nums = []
nums.append(int(input()))

for _ in range(N-1):
    start = 0 
    end = len(nums) - 1 
    
    next_n = int(input())
    
    while start <= end:
        mid = (start + end) // 2
        
        if nums[mid] >= next_n:
            end = mid - 1
            
        else:
            start = mid + 1 
            
    nums = nums[ : end+1] + [next_n] + nums[end+1:] 
    
    if len(nums) % 2 == 1 :
        print(nums[len(nums)//2])
    else:
        print(nums[len(nums)//2-1])