#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:57:35 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

S = 0 

M = int(input())

for _ in range(M):
    command = input().strip().split()
    func = command[0]
    if func != "all" and func != "empty":
        val = int(command[1])
    
    if func == "add":
        if not S & 1 << (val - 1):
            S += 1 << (val - 1)
            
    elif func == "remove":
        if S & 1 << (val - 1):
            S -= 1 << (val - 1)
            
    elif func == "check":
        if S & 1 << (val - 1):
            print(1)
        else:
            print(0)
            
    elif func == "toggle":
        if S & 1 << (val - 1):
            S -= 1 << (val - 1)
        else:
            S += 1 << (val - 1)
    
    elif func == "all":
        S = 2 ** 20 - 1
    
    else:
        S = 0
        
        
