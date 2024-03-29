#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:02:54 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline

N, M, K = map(int, input().split())

land = [[5 for _ in range(N)] for _ in range(N)]

A = []
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

for _ in range(N):
    A.append(list(map(int, input().split())))
    
tree = []

for _ in range(M):
    tree.append(list(map(int, input().split())))
    
tree.sort(key=lambda x: -x[2])
    
def spring_summer():
    die = []
    for i in range(len(tree)-1, -1, -1):
        r, c, age = tree[i]
        r -= 1 
        c -= 1 
        if land[r][c] >= age:
            land[r][c] -= age
            tree[i][2] += 1
        else:
            tree.pop(i)
            die.append([r, c, age // 2])
            
    for j in die:
        r, c, food = j 
        r -= 1
        c -= 1 
        land[r][c] += food
        
    return

def autumn():
    for i in range(len(tree)):
        r, c, age = tree[i]
        r -= 1 
        c -= 1 
        if age % 5 == 0:
            for j in range(8):
                rr = r + dx[j]
                cc = c + dy[j]
                if 0 <= rr < N  and 0 <= cc < N:
                    tree.append([rr+1, cc+1, 1])
        if age < 5:
            break
            
def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]

for i in range(K):
    spring_summer()
    autumn()
    winter()
    
print(len(tree))   