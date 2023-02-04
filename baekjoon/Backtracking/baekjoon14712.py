N, M = map(int, input().split())

board = [[0 for _ in range(M+1)] for _ in range(N+1)]

def Backtracking(x, y):
    global answer 

    if board[x-1][y-1] + board[x][y-1] + board[x-1][y] !=3:
        board[x][y] = 1 
        answer += 1 
        if y != M:
            Backtracking(x, y+1)
        if x != N:
            Backtracking(x+1, y)
        if x != N and y != M:
            Backtracking(x+1, y+1)
        board[x][y] = 0
            
    if y != M:
        Backtracking(x, y+1)
    if x != N:
        Backtracking(x+1, y)
    if x != N and y != M:
        Backtracking(x+1, y+1)
            
    




answer = 0 

Backtracking(1, 1)

print(answer)