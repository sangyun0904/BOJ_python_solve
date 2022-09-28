#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:03:11 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

parents = [str(i) for i in range(N)]

def find(n):
    if parents[n] == str(n):
        return n 
    else:
        return find(int(parents[n]))
    
def merge(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parents[b] = str(a)
    else:
        parents[a] = str(b) 
     
sort_game = []

for _ in range(M):
    a, op, b = input().strip().split() 
    a = int(a)
    b = int(b)
    
    if op == "=":
        merge(a,b)
    else:
        sort_game.append([a, b])
        
graph = {str(i):0 for i in range(N)}

def chess_tournament(sort_game):
    for a, b in sort_game:
        a = str(find(a))
        b = str(find(b))
        
        if a == b:
            return "inconsistent"
        elif graph[b] > graph[a]:
            return "inconsistent"
        elif graph[b] == graph[a]:
            graph[a] += 1
            
    return "consistent"

print(chess_tournament(sort_game))
        
    
    
    
    