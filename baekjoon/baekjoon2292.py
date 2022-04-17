# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:58:57 2022

@author: USER
"""

N = int(input())

cnt = 0
step = 0

while True: 
    step += cnt 
    if step * 6 + 1 >= N:
        break 
    cnt += 1 
    
print(cnt + 1)