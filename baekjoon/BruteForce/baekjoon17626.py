# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:27:36 2022

@author: USER
"""

n = int(input())

square_nums = []

for i in range(1, 244):
    square_nums.append(i*i)

def answer(n):
    
    if n in square_nums:
        return 1 
    else:
        for i in square_nums:
            if n > i:
                if n - i in square_nums:
                    return 2 
            else:
                break 
            
        for i in range(243):
            for j in range(i, 243):
                if n > square_nums[i]+square_nums[j] :
                    if n - square_nums[i] - square_nums[j] in square_nums:
                        return 3
                else:
                    break 
            
    return 4 

print(answer(n))