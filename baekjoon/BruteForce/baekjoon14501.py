#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:01:39 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

time = []
money = []

for _ in range(N):
    t, m = map(int, input().split())
    
    time.append(t)
    money.append(m)
    
ans = 0

def work(day, cur):
    global ans
    
    if ans < cur:
        ans = cur
        
    if day >= N:
        return
    
    t = time[day]
    m = money[day]
        
    if t <= N - day:
        work(day+t, cur+m)
    
    work(day+1, cur)
    
    return
    
work(0, 0)
    
print(ans)