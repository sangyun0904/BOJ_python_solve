#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:37:33 2022

@author: sangyoon
"""

#import sys 
#input = sys.stdin.readline 

N = int(input())

times = list(map(int, input().split()))

times.sort()

ans = 0

for i in range(N):
    ans += sum(times[:i+1])
    
print(ans)