#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:44:29 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

_ = int(input())
A = list(map(int, input().split()))

def getDescLen(A, idx):
    memo = [[] for _ in range(idx, len(A))]
    memo[0].append(A[idx])
    cnt = 1
    for i in range(idx, len(A)):
        for j in memo:
            if j != []:
                if A[i] > memo[cnt-1][-1] and A[i] < A[idx]:
                    for m in memo[0]:
                        if m > A[i]:
                            memo[cnt].append(m)
                    cnt += 1
                if A[i] < j[-1]:
                    j.append(A[i])
    return max(memo, key=lambda x:len(x))
    
answers = []   
 
for i in range(len(A)):
    l1 = getDescLen(A, i)
    A.reverse()
    l2 = getDescLen(A, len(A)-i-1)
    A.reverse()
    
    answers.append(len(l1) + len(l2) - 1)

print(max(answers))