# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:18:10 2022

@author: USER
"""

import sys 

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 
    
    if r1 > dist or r2 > dist: 
        if dist == 0 and r1 == r2:
            print(-1)
        elif dist < max([r1, r2]) - min([r1, r2]):
            print(0)
        elif dist == max([r1, r2]) - min([r1, r2]):
            print(1)
        else:
            print(2)
    else:
        if dist > r1 + r2:
            print(0)
        elif dist == r1 + r2:
            print(1)
        else:
            print(2)