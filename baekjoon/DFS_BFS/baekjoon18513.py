import sys 
from collections import deque 
input = sys.stdin.readline 

N, K = map(int, input().split())

samters = list(map(int, input().split()))

visited = {}
q = deque()
answer = 0 
cnt = 0

for i in samters:
    visited[i] = True 
    q.append([i, 0])

while q:
    x, dist = q.popleft()
    if x-1 not in visited:
        visited[x-1] = True 
        answer += dist+1 
        q.append([x-1, dist+1])
        cnt += 1 
        if cnt == K:
            break

    if x+1 not in visited:
        visited[x+1] = True 
        answer += dist+1 
        q.append([x+1, dist+1])
        cnt += 1 
        if cnt == K:
            break

print(answer)