# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:44:00 2022

@author: USER
"""
N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list_len = len(n_list)

answer = 0
for i in range(n_list_len):
    for j in range(i+1, n_list_len):
        for k in n_list[j+1: ]:
            temp = n_list[i] + n_list[j] + k
            if temp > answer and temp <= M:
                answer = temp
                
print(answer)