#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:07:54 2022

@author: sangyoon
"""

import sys 

MAX_N = 10000 

prime_list = [True] * (MAX_N + 1)

prime_list[1] = False

for i in range(1, MAX_N + 1):
    if prime_list[i]:
        j = 2 
        while True:
            if i * j > MAX_N:
                break 
            prime_list[i * j] = False 
            j += 1 
            
T = int(sys.stdin.readline()) 

for _ in range(T):
    N = int(sys.stdin.readline())
    
    prime1, prime2 = 0, 0
    
    for i in range(2, N // 2 + 1):
        if prime_list[i]:
            if prime_list[N - i]:
                prime1 = i 
                prime2 = N - i
                
    print(prime1, prime2)