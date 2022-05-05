# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:51:43 2022

@author: USER
"""
import sys
input = sys.stdin.readline 

N = int(input())
n_list = list(map(int, input().split()))
answer = [0]

for i in n_list:
    if i > answer[-1]:
        answer.append(i)
    else:
        start = 0
        end = len(answer)-1
        while start < end:
            mid = (start + end) // 2
            if answer[mid] < i:
                start = mid + 1
            else:
                end = mid
        answer[end] = i 
print(answer)