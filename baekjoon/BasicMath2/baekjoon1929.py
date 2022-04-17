#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:59:22 2022

@author: sangyoon
"""

import sys 

#M, N = map(int, sys.stdin.readline().split())

M, N = map(int, input().split())

primes = [True] * (N + 1)

for i in range(2, N):
    if primes[i] == True:
        j = 2
        
        while (i * j) <= N:
            primes[i * j] = False 
            j += 1
            
for num in range(M, len(primes)):
    if primes[num]:
        print(num)