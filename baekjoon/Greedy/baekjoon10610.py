#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 20:02:24 2022

@author: sangyoon
"""

N = int(input())

def answer(n):
    if n % 3 != 0:
        return -1
    
    n = list(str(n))
        
    n.sort(reverse=True)
    
    if n[-1] != "0":
        return -1 
    else:
        ans = int("".join(n))
        return ans

print(answer(N))