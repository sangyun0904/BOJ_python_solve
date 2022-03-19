# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:37:18 2022

@author: USER
"""

import sys 

_ = sys.stdin.readline()

nList = list(map(int, sys.stdin.readline().split()))

cnt = 0 

for i in nList:
    cnt += 1
    if i == 1:
        cnt -= 1 
    for j in range(2 , i):
        if i % j == 0:
            cnt -= 1
            
print(cnt)