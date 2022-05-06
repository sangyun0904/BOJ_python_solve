# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:31:25 2022

@author: USER
"""

def solution(stones, k):
    answer = 0
    start = 0 
    end = max(stones)
    while start <= end:
        mid = (start+end) // 2 
        cnt = 0 
        for i in stones:
            if i-mid < 0:
                cnt += 1 
            else:
                cnt = 0
            if cnt == k:
                break
        if cnt == k :
            end = mid - 1
        else:
            start = mid + 1
    answer = end
    return answer