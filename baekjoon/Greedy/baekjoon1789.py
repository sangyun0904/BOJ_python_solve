#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:09:45 2022

@author: sangyoon
"""

S = int(input())

ans = 0 
i = 1 

while True:
    S -= i 
    if S <= 0 :
        break
    ans += 1 
    i += 1 

print(ans)