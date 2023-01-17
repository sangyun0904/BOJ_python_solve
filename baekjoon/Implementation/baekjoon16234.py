import sys 
from collections import deque
input = sys.stdin.readline 

N, L, R = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i, j):
    ret = []
    visited[i][j] = True

    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N:
                if not visited[xx][yy]:
                    if L <= abs(board[x][y] - board[xx][yy]) <= R:
                        visited[xx][yy] = True
                        q.append([xx, yy])
                        ret.append([xx, yy])

    return ret

def getAvg(x, y, connected):
    ret = board[x][y]

    for i, j in connected:
        ret += board[i][j]
    
    ret = ret // (len(connected) + 1)

    for i, j in connected:
        board[i][j] = ret  

    return ret  


cnt = 0
moving = True

while moving:
    moving = False

    visited = [[False for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            connected = []

            if not visited[i][j]:
                connected = BFS(i, j)
                if connected != []:
                     moving = True

                board[i][j] = getAvg(i, j, connected)

    if moving:
        cnt += 1

                     
print(cnt)