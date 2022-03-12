#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:31:56 2022

@author: sangyoon
"""
# DFS 메서드 정의
def dfs(graph, current, visited) :
    # 형제 노드를 방문 처리
    visited[current] = True 
    print(current, end=" ")
    # 현제 노드와 연결도니 다른 노드를 재귀적으로 방문
    for i in graph[current] :
        if not visited[i] :
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1,7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문한 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출 
dfs(graph, 1, visited)
