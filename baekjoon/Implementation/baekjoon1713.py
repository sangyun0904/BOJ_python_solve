N = int(input())
M = int(input())
recommend = list(map(int, input().split()))

candid = []

for i in recommend:
    isCandid = False
    for j in range(len(candid)):
        n, count, time = candid[j] 
        if i == n:
            candid[j][1] -= 1 
            isCandid = True
        candid[j][2] += 1
    
    if not isCandid:
        if len(candid) == N:
            candid.pop()
        candid.append([i, -1, 0])
    
    candid.sort(key=lambda x : [x[1], x[2]])

answer = []

for i in candid:
    answer.append(i[0])

answer.sort()
for i in answer:
    print(i , end=" ")