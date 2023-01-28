import sys 
input = sys.stdin.readline 

MAX_DIST = 1000000

N = int(input())

cities = []

for _ in range(N):
    cities.append(list(map(int, input().split())))

for i in cities:
    print(i)

def Backtracking(n, d):
    if visited == [True, True, True, True]:
        if d < answer:
            answer = d 
            return 
        


answer = MAX_DIST * N 

for i in range(N):
    visited = [False for _ in range(N)]
    Backtracking(i)