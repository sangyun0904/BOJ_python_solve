import sys 
input = sys.stdin.readline

N = int(input())
Time = []
Pay = []

for _ in range(N):
    t, p = map(int, input().split())
    Time.append(t)
    Pay.append(p)

memo = [0 for _ in range(N+1)]

for i in range(N):
    if i > 0 and memo[i-1] > memo[i]:
        memo[i] = memo[i-1]

    if i + Time[i] <= N and memo[i+Time[i]] < memo[i] + Pay[i]:
        memo[i+Time[i]] = memo[i] + Pay[i]

print(max(memo[-1], memo[-2]))