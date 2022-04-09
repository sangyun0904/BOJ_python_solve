# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:03:03 2022

@author: USER
"""

def backTracking(rowPos):
    global answer  
    
    # 퀸을 모두 배치했다면 끝
    if rowPos == n:
        answer += 1
        return
    
    for col in range(n):
        flag = True
        # 이전 행들에 대해서
        for row in range(rowPos):
            # 같은 열에 위치해있거나 대각선에 퀸이 이미 존재한다면 가지치기
            if queenLocation[row] == col or rowPos - row == abs(col - queenLocation[row]):
                flag = False
                break
        if flag:
            queenLocation[rowPos] = col
            backTracking(rowPos + 1)
    
n = int(input())
answer = 0
# 각 row마다 queen이 위치하는 인덱스를 저장하는 리스트
queenLocation = [0] * n
backTracking(0)
print(answer)