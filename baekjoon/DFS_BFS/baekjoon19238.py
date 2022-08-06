# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:55:02 2022

@author: USER
"""

import sys 
from collections import deque
input = sys.stdin.readline 

N, M, F = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
start = list(map(int, input().split()))
start[0] -= 1
start[1] -= 1

for i in range(M):
    customer = list(map(int, input().split()))
    graph[customer[0]-1][customer[1]-1] = str(customer[2]-1) + " " + str(customer[3]-1)

    
def move(start):
    if graph[start[0]][start[1]] != 0:
        return [start, 0]
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([[start, 0]])
    visited[start[0]][start[1]]
    res = []
    while q:
        cur, d = q.popleft() 
        x = cur[1]
        y = cur[0]
        for i in range(4):
            xx = dx[i] + x 
            yy = dy[i] + y 
            if 0 <= xx < N and 0 <= yy < N:
                if graph[yy][xx] != 1 and not visited[yy][xx]:
                    if graph[yy][xx] != 0:
                        res.append([(yy, xx), d+1])
                    else:
                        visited[yy][xx] = True
                        q.append([(yy, xx), d+1])
    if res == []:
        return -1
    else:
        res.sort(key = lambda x : (x[1], x[0][0], x[0][1]))
        return res[0]
                        
def ride(start, target):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([[start, 0]])
    visited[start[0]][start[1]]
    while q:
        cur, d = q.popleft() 
        x = cur[1]
        y = cur[0]
        for i in range(4):
            xx = dx[i] + x 
            yy = dy[i] + y 
            if 0 <= xx < N and 0 <= yy < N:
                if graph[yy][xx] != 1 and not visited[yy][xx]:
                    if [yy, xx] == target:
                        return [(yy, xx), d+1]
                    else:
                        visited[yy][xx] = True
                        q.append([(yy, xx), d+1])    
    return -1
                        
while F > 0:
    res = move(start)
    if res == -1 :
        F = -1
    else:
        if res[1] > F:
            F = -1
        else:
            target = list(map(int, graph[res[0][0]][res[0][1]].split()))
            graph[res[0][0]][res[0][1]] = 0
            F -= res[1]
            start = res[0]
            res = ride(start, target)
            
            if res == -1:
                F = -1
            else:
                if res[1] > F:
                    F = -1 
                else:
                    graph[res[0][0]][res[0][1]] = 0
                    F += res[1]
                    start = res[0]
                    M -= 1
    if M == 0 :
        break

print(F)         