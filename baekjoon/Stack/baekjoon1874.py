# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:20:07 2022

@author: USER
"""

import sys 
input = sys.stdin.readline 

N = int(input())

stack = []
nextNum = 1
answer = []
ispossible = True

for _ in range(N):
    num = int(input())
    if num >= nextNum:
        while num >= nextNum:
            stack.append(nextNum)
            nextNum += 1 
            answer.append("+")
            
    if stack[-1] != num:
        ispossible = False 
    else:
        stack.pop()
        answer.append("-")
    
if ispossible:
    for i in answer:
        print(i)
else:
    print("NO")