# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:11:27 2022

@author: USER
"""

def solution(n, k, cmd):
    answer = ''
    linked = {i : [i-1, i+1] for i in range(n)}
    linked[n-1][1] = -1 
    delNode = []
    isDel = [False for _ in range(n)]
    for c in cmd:
        if c[0] == 'D':
            for i in range(int(c.split()[-1])):
                k = linked[k][1]
        if c[0] == 'U':
            for i in range(int(c.split()[-1])):
                k = linked[k][0]
        if c == 'C':
            if linked[k][0] != -1:
                linked[linked[k][0]][1] = linked[k][1]
            if linked[k][1] != -1:
                linked[linked[k][1]][0] = linked[k][0]
            delNode.append(k)
            isDel[k] = True
            if linked[k][1] == -1:
                k = linked[k][0]
            else:
                k = linked[k][1]
        if c == 'Z':
            idx = delNode.pop()
            isDel[idx] = False
            if linked[idx][0] != -1:
                linked[linked[idx][0]][1] = idx
            if linked[idx][1] != -1:
                linked[linked[idx][1]][0] = idx
    
    for i in range(n):
        if isDel[i]:
            answer += 'X'
        else: 
            answer += 'O'
            
    return answer

n = 8
k = 2 
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))