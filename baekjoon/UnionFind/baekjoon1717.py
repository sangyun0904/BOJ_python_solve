#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:13:40 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

def find_parent(a):
    while a != graph[a]:
        a = graph[a]
    return a
        

def func_1(a, b):
    return find_parent(a) == find_parent(b)

def func_0(a, b):
    p1 = find_parent(a)
    p2 = find_parent(b)
    if p1 < p2:
        graph[p2] = p1
    else:
        graph[p1] = p2

n,m = map(int, input().split())
graph = [i for i in range(0, n+1)]
for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        func_0(a, b)
    else:
        if func_1(a, b):
            print("YES")
        else:
            print("NO")
for i in range(1, n+1):
    print(find_parent(i))