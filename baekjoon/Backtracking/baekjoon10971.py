import sys 
input = sys.stdin.readline 

MAX_DIST = 1000000

N = int(input())

cities = []

for _ in range(N):
    cities.append(list(map(int, input().split())))


def Backtracking(n, d, bitmask):
    global answer
    if bitmask == 2**N-1:
        if cities[n][start] != 0:
            if d + cities[n][start] < answer:
                answer = d + cities[n][start]
        return 
    else:
        for i in range(N):
            if not bitmask & (1<<i) and cities[n][i] != 0:
                Backtracking(i, d+cities[n][i], bitmask + (1<<i))

    return
        

start = 0
answer = MAX_DIST * N 

for i in range(N):
    start = i
    bitmask = 1 << i
    Backtracking(i, 0, bitmask)


print(answer)