import sys 
input = sys.stdin.readline 
n, m = map(int, input().split())
deudbo = {}
for _ in range(n):
    temp = input().strip()
    deudbo[temp] = True

cnt = 0
ans = []

for _ in range(m):
    temp = input().strip() 
    if temp in deudbo:
        cnt += 1 
        ans.append(temp)

print(cnt)
ans.sort()
for i in ans:
    print(i)