# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:44:13 2022

@author: USER
"""

import sys 
input = sys.stdin.readline

nums = []

for _ in range(9):
    n = int(input())
    nums.append(n)
    
s = sum(nums)
ans = []

for i in range(8):
    for j in range(i+1, 9):
        temp = s 
        temp -= nums[i] + nums[j]
        if temp == 100:
            ans.append(nums[i])
            ans.append(nums[j])
for i in ans:
    nums.remove(i)
            
nums.sort()
for i in nums:
    print(i)