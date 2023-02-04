import sys
input = sys.stdin.readline 

T = int(input())

position = [0 for _ in range(11)]
inPosition = [False for _ in range(11)]

def DFS(pos):
    global answer

    if pos == 11:
        if answer < sum(position):
            answer = sum(position)
        return

    for i in range(11):
        if not inPosition[i] and players[i][pos] != 0:
            position[pos] = players[i][pos]
            inPosition[i] = True
            DFS(pos+1)
            position[pos] = 0 
            inPosition[i] = False 

for _ in range(T):
    players = []
    for _ in range(11):
        players.append(list(map(int, input().split())))

    answer = 0 

    DFS(0)

    print(answer)