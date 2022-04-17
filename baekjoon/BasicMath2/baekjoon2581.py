# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:55:22 2022

@author: USER
"""

import sys 

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())

first_prime = -1
prime_sum = 0

for i in range(n1, n2+1):
    isPrime = True 
    if i == 1:
        isPrime = False
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        if first_prime == -1:
            first_prime = i 
        prime_sum += i

if first_prime == -1:
    print(-1)
else:
    print(prime_sum)
    print(first_prime)