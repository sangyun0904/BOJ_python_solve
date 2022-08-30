#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:36:05 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

def R(array):
    
    new_array = []
    
    for i in array:
        vals = list(set(i))
        cnts = []
        
        for j in vals:
            if j != 0 :
                cnts.append([i.count(j), j])
                
        cnts.sort() 
        sorted_i = []
        
        for j in cnts:
            sorted_i.append(j[1])
            sorted_i.append(j[0])
            
        if len(sorted_i) > 100:
            sorted_i = sorted_i[:100]
        
        new_array.append(sorted_i)
        
    max_len = max([len(i) for i in new_array])
        
    for i in new_array:
        for _ in range(max_len - len(i)):
            i.append(0)
            
    return new_array

r, c, k = map(int, input().split())

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
  
ans = -1
  
for i in range(101):
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]):
        if A[r-1][c-1] == k:
            ans = i
            break
        
    if len(A) >= len(A[0]):
        A = R(A)
    else:
        A = list(map(list, zip(*A)))
        A = R(A)
        A = list(map(list, zip(*A)))
    
print(ans)
        
