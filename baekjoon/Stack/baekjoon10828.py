#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:11:58 2022

@author: sangyoon
"""
import sys 
input = sys.stdin.readline 

stack = []
top = -1 

N = int(input())

for _ in range(N):
    command = list(input().strip().split())
    if command[0] == "push":
        data = int(command[1])
        stack.append(data)
        top += 1 
    elif command[0] == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    else:
        if top == -1:
            print(-1)
        else:
            print(stack[top])