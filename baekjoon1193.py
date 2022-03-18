# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:09:45 2022

@author: USER
"""

N = int(input()) 

cnt = 1
step = 0

while True:
    step += cnt
    if step > N:
        break
    cnt += 1
    
