# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:46:05 2022

@author: USER
"""

#import sys
#input = sys.stdin.readline

def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]: 
            continue

        rows[x] = i
        if check(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False

n = int(input())
rows = [0] * n
visited = [False] * n
cnt = 0

dfs(0)
print(cnt)