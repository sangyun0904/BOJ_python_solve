#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:31:46 2022

@author: sangyoon
"""

import sys 

house, router = map(int, sys.stdin.readline().split())

house_list = []

for _ in range(house):
    house_list.append(int(sys.stdin.readline()))
    
house_list.sort()

def binary_search(start, end):
    mid = (start + end) // 2
    while start <= end:
        current = house_list[0]
        cnt = 1
        for i in house_list:
            if i - current >= mid:
                cnt += 1
                current = i
        
        if cnt >= router:
            start = mid + 1
        else:
            end = mid - 1
            
        mid = (start + end) // 2
            
    return mid

print(binary_search(1, house_list[-1] - house_list[0]))