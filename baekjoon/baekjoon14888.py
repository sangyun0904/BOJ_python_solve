#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:02:45 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

INF = sys.maxsize

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # ['+','-','*','/']

ans1 = -INF 
ans2 = INF 

def BT(cur, depth): # nums[0], 1
    global ans1, ans2

    if depth == N:
        if ans1 < cur:
            ans1 = cur
        if ans2 > cur:
            ans2 = cur
        return
    
    if ops[0] > 0:
        ops[0] -= 1
        BT(cur + nums[depth], depth+1)
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        BT(cur - nums[depth], depth+1)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        BT(cur * nums[depth], depth+1)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        if cur < 0:
            BT(-(-cur // nums[depth]), depth+1)
        else:
            BT(cur // nums[depth], depth+1)
        ops[3] += 1
            
BT(nums[0], 1)

print(ans1)
print(ans2)