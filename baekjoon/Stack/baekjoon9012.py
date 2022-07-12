# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:16:55 2022

@author: USER
"""

import sys 

input = sys.stdin.readline 

N = int(input())

for _ in range(N):
    line = input().strip() 
    stack = []
    answer = "YES"
    
    for i in line:
        if i == "(":
            stack.append(i)
        else:
            if stack != []:
                stack.pop()
            else:
                answer = "NO"
    if stack != []:
        answer = "NO"
        
    print(answer)
