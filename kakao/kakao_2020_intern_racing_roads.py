#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:40:30 2022

@author: sangyoon
"""

import heapq

INF = int(1e9)

def dijkstra(start, dist, graph, prev_nodes):
    q = []
    dist[start[1]][start[0]] = 0
    
    heapq.heappush(q, [0, start])
    while q:
        d, cur = heapq.heappop(q)
        for n in graph[cur[1]][cur[0]]:
            if cur == (0,0):
                cost = 100 + d
            else:
                if prev_nodes[cur[1]][cur[0]][0] == n[0] or prev_nodes[cur[1]][cur[0]][1] == n[1]:
                    cost = d + 100
                else:
                    cost = d + 600 
            if dist[n[1]][n[0]] > cost:
                dist[n[1]][n[0]] = cost
                heapq.heappush(q, [cost, n])
                prev_nodes[n[1]][n[0]] = cur
            
    

def solution(board):
    answer = 0
    N = len(board)
    graph = [[[] for _ in range(N)] for _ in range(N)]
    prev_nodes = [[None for _ in range(N)] for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if i > 0:
                    if board[i-1][j] == 0:
                        graph[i][j].append((j, i-1))
                if j > 0:
                    if board[i][j-1] == 0:
                        graph[i][j].append((j-1, i))
                if i < N-1:
                    if board[i+1][j] == 0:
                        graph[i][j].append((j, i+1))
                if j < N-1:
                    if board[i][j+1] == 0:
                        graph[i][j].append((j+1, i))
    dijkstra((0,0), dist, graph, prev_nodes)
    answer = dist[N-1][N-1]
    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]

print(solution(board))







