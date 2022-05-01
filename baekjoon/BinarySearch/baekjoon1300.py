# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:03:40 2022

@author: USER
"""

#import sys 
#input = sys.stdin.readline 

N = int(input())
k = int(input())

def binary(start, end, k):
    while start <= end:
        mid = (start + end) // 2 
        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid // i, N) 
        if cnt < k:
            start = mid + 1 
        elif cnt > k:
            end = mid - 1
        else:
            
    return mid

start = 1 
end = N ** 2

print(binary(1, N**2, k))