import sys 
input = sys.stdin.readline 

R, C = map(int, input().split())
board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board.append("."*(C + 2))
for _ in range(R):
    board.append("." + input().strip() + ".")
board.append("."*(C + 2))

new_map = [["." for _ in range(C+2)] for _ in range(R+2)]

for i in range(R+2):
    for j in range(C+2):
        if board[i][j] == "X":
            cnt = 0 
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if board[xx][yy] == ".":
                    cnt += 1 

            if cnt < 3:
                new_map[i][j] = "X"

xs = C + 2
xe = 0
ys = R + 2
ye = 0 

for i in range(R + 2):
    for j in range(C + 2):
        if new_map[i][j] == "X":
            if i < ys:
                ys = i 
            if i > ye:
                ye = i 
            if j < xs:
                xs = j 
            if j > xe:
                xe = j 

for i in range(ys, ye+1):
    print("".join(new_map[i][xs:xe+1]))