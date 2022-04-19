#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:54:40 2022

@author: sangyoon
"""

def solution(food_times, k):
    answer = 0
    cutting, idx = binary_search(food_times, k)
    food_times = [i-cutting for i in food_times]
    
    for i in range(len(food_times)):
        if food_times[i] > 0 and idx == k:
            answer = i+1
            return answer
        else:
            if food_times[i] > 0:
                idx += 1
        
    return -1

def binary_search(food_times, k):
    low, high = 0, 1000000000
    n, cutting, idx = len(food_times), 0, 0
    while low <= high:
        mid = (low + high) // 2
        v = n * mid
        for f in food_times:
            tmp = f - mid
            if tmp < 0 :
                v += tmp
        if v <= k:
            cutting, idx = mid, v
            low = mid + 1
        else:
            high = mid - 1
    return cutting, idx