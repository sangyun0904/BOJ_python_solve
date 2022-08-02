#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:48:48 2022

@author: sangyoon
"""

n = int(input()) 

money = [500, 100, 50, 10, 5, 1]

remain = 1000 - n 

ans = 0 

for m in money:
    temp = remain // m 
    remain -= temp * m 
    ans += temp
    
print(ans)