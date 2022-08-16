#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:46:58 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

dice = list(map(int, input().split()))
start0 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 46, 38, 40, 0]
start10 = [10, 13, 16, 19, 25, 30, 35, 40, 0]
start20 = [20, 22, 24, 25, 30, 35, 40, 0]
start30 = [30, 28, 27, 26, 25, 30, 35, 40, 0]
board = [start0, start10, start20, start30]

ans = 0     

def BackTracking(locs, total, depth):
    global ans
    
    if depth == 10:
        if total > ans:
           ans = total
        return
       
    for i in range(4):
        if locs[i][0] == 0:
            if locs[i][1] == 5 :
                locs[i][0] = 1
                locs[i][1] = dice[depth]
                if dice[depth] >= 4:
                    cnt = locs.count([1,dice[depth]]) + locs.count([2,dice[depth]-1]) + locs.count([3,dice[depth]])
                else:
                    cnt = locs.count(locs[i])
                if cnt == 1:
                    BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                locs[i][0] = 0
                locs[i][1] = 5
            elif locs[i][1] == 10 :
                locs[i][0] = 2
                locs[i][1] = dice[depth]
                if dice[depth] >= 3:
                    cnt = locs.count([1,dice[depth]+1]) + locs.count([2,dice[depth]]) + locs.count([3,dice[depth]+1])
                else:
                    cnt = locs.count(locs[i])
                if cnt == 1:
                    BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                locs[i][0] = 0
                locs[i][1] = 10
            elif locs[i][1] == 15 :
                locs[i][0] = 3
                locs[i][1] = dice[depth]
                if dice[depth] >= 4:
                    cnt = locs.count([1,dice[depth]]) + locs.count([2,dice[depth]-1]) + locs.count([3,dice[depth]])
                else:
                    cnt = locs.count(locs[i])
                if cnt == 1:
                    BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                locs[i][0] = 0
                locs[i][1] = 15
            else:
                if len(board[0]) - 1 > locs[i][1] + dice[depth]:
                    locs[i][1] += dice[depth]
                    if dice[depth] == 20:
                        cnt = locs.count([1,7]) + locs.count([2,6]) + locs.count([3,7]) + locs.count([0,20])
                    else:
                        cnt = locs.count(locs[i])
                    if cnt == 1:
                        BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                    locs[i][1] -= dice[depth]
                else:
                    temp = locs[i][1]
                    locs[i][1] = len(start0) - 1
                    BackTracking(locs, total, depth+1)
                    locs[i][1] = temp
        else:
            if len(board[locs[i][0]]) - 1 > locs[i][1] + dice[depth]:
                locs[i][1] += dice[depth]
                if locs[i][0] == 2:
                    if locs[i][1] == 6:
                        cnt = locs.count([1,7]) + locs.count([2,6]) + locs.count([3,7]) + locs.count([0,20])
                    elif locs[i][1] >= 3:
                        cnt = locs.count([1,locs[i][1]+1]) + locs.count([2,locs[i][1]]) + locs.count([3,locs[i][1]+1])
                    else:
                        cnt = locs.count(locs[i])
                    if cnt == 1:
                        BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                else:
                    if locs[i][1] == 7:
                        cnt = locs.count([1,7]) + locs.count([2,6]) + locs.count([3,7]) + locs.count([0,20])
                    elif locs[i][1] >= 4:
                        cnt = locs.count([1,locs[i][1]]) + locs.count([2,locs[i][1]-1]) + locs.count([3,locs[i][1]])
                    else:
                        cnt = locs.count(locs[i])
                    if cnt == 1:
                        BackTracking(locs, total + board[locs[i][0]][locs[i][1]], depth+1)
                locs[i][1] -= dice[depth]
            else:
                temp = locs[i][1]
                locs[i][1] = len(board[locs[i][0]]) - 1
                BackTracking(locs, total, depth+1)
                locs[i][1] = temp
                
BackTracking([[0,0],[0,0],[0,0],[0,0]], 0, 0)
          
print(ans)



