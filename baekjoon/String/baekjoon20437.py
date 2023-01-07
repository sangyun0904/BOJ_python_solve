import sys 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    s = input().strip()
    k = int(input())

    ans = []

    cnts = {}

    for i in range(len(s)):
        if s[i] in cnts:
            cnts[s[i]].append(i)
        else:
            cnts[s[i]] = [i]

    for l in cnts.values():
        if len(l) >= k:
            for i in range(len(l) - k + 1):
                ans.append(l[i+k-1] - l[i]+1)

    if ans == []:
        print(-1)
    else:
        ans.sort()
        print(ans[0], ans[-1])
