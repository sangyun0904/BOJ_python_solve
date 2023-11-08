import sys
input = sys.stdin.readline

N, X = map(int, input().split())

visitors = list(map(int, input().split()))
max_visit = sum(visitors[0:X])
cur_visit = sum(visitors[0:X])
cnt = 0

print("visitors:", visitors)
print("max_visit:", max_visit)
print("cur_visit:", cur_visit)
print("cnt:", cnt)

for i in range(len(visitors) - X):
    cur_visit += visitors[i + X]
    cur_visit -= visitors[i]

    if cur_visit == max_visit:
        cnt += 1
    elif cur_visit > max_visit:
        max_visit = cur_visit
        cnt = 1
    print("max_visit:", max_visit)
    print("cur_visit:", cur_visit)
    print("cnt:", cnt)

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)