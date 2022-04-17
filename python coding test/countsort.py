#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:30:21 2022

@author: sangyoon
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
sortedArray = []


count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        sortedArray.append(i)
        
print(sortedArray)