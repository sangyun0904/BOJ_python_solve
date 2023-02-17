import sys 
input = sys.stdin.readline 

N = int(input())

jump = []

for _ in range(N-1):
    jump.append(list(map(int, input().split())))

k = int(input())

memo = [[0,0] for _ in range(N)] # [매우 큰 점프 안쓴 에너지, 매우 큰 점프 쓴 에너지]

for i in range(1, N):
    if i == 1:
        memo[i] = [jump[i-1][0], 0]
    elif i == 2:
        memo[i] = [min(memo[i-1][0]+jump[i-1][0], jump[i-2][1]), 0]
    else:
        # [ min( 바로앞 메모 매우 큰 점프 (x) + 작은점프, 전전메모 매우 큰 점프 (x) + 큰 점프),
        #   min( 바로앞 메모 매우 큰 점프 (o) + 작은점프, 전전메모 매우 큰 점프 (o) + 큰 점프, 전전전메모 매우큰점프(x) + 매우큰 점프(k) )]
        notK = min(memo[i-1][0]+jump[i-1][0], memo[i-2][0]+jump[i-2][1])
        if memo[i-1][1] == 0:
            didK = k 
        elif memo[i-2][1] == 0:
            didK = min(memo[i-1][1]+jump[i-1][0], memo[i-3][0]+k)
        else:
            didK = min(memo[i-1][1]+jump[i-1][0], memo[i-2][1]+jump[i-2][1], memo[i-3][0]+k)
        memo[i] = [notK,didK] 

if min(memo[-1]) != 0:
    print(min(memo[-1]))
else:
    print(memo[-1][0])