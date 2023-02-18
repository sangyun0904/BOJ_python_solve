import sys 
from collections import deque
input = sys.stdin.readline 

MAX_DIST = sys.maxsize
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append([i, j, 0])
            board[i][j] = 0
        elif board[i][j] == 1:
            board[i][j] = MAX_DIST

while q:
    x, y, d = q.popleft() 
    for k in range(4):
        xx = dx[k] + x 
        yy = dy[k] + y 

        if 0 <= xx < n and 0 <= yy < m:
            if d+1 < board[xx][yy]:
                board[xx][yy] = d+1
                q.append([xx, yy, d+1])

for i in range(n):
    for j in range(m):
        if board[i][j] == MAX_DIST:
            board[i][j] = -1

for i in board:
    for j in i:
        print(j, end=" ")
    print()