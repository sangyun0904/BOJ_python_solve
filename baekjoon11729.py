# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:20:20 2022

@author: USER
"""
move = []

def hanoi(N, start, mid, end):
    if N == 1 :
        move.append([start, end])
        return
    else:
        hanoi(N-1, start, end, mid)
        move.append([start, end])
        hanoi(N-1, mid, start, end)
        
N = int(input())

hanoi(N, 1, 2, 3)
print(len(move))
for i in move:
    print(i[0], i[1])