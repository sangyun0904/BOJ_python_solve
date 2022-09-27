#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:39:50 2022

@author: sangyoon
"""

# 특정 원소가 속한 집합을 찾기

def find(x):
    
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출 
    if parent[x] != x:
        return find(parent[x])
    return x

#두 원소가 속한 집합을 합치기 
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 
        
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기 
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기 

# 부모 테미블상에서, 부모를 자기 자신으로 초기화 
for i in range(1, v + 1):
    parent[i] = i 
    
# Union 연산을 각각 수행 
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)
    
# 각 원소가 속한 집합 출력하기 
print('각 원소가 속한 집합: ', end="")
for i in range(1, v + 1):
    print(find(i), end=' ')
    
print()

# 부모 테이블 내용 출력하기 
print('부모 테이블: ', end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")