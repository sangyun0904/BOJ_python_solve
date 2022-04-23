#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:05:57 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

price = cities[0]
ans = 0

for i in range(len(roads)):
    if cities[i] < price:
        price = cities[i]
    
    ans += price * roads[i]
    
print(ans)