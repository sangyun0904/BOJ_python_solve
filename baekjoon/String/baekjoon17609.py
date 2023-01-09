import sys 
input = sys.stdin.readline 

def isPalin(strin):
    cnt = 0 
    char_cnt = {}
    for i in strin:
        if i in char_cnt:
            char_cnt[i] += 1
        else:
            char_cnt[i] = 1
    s = 0 
    e = len(strin)-1 
    while e > s :
        if strin[s] == strin[e]:
            s += 1 
            e -= 1 
        elif cnt == 1:
            return 2 
        elif char_cnt[strin[s]] % 2 == 1 and char_cnt[strin[e]] % 2 == 1:
            s += 1 
            e -= 1 
            cnt += 1
        elif char_cnt[strin[s]] % 2 == 1:
            s += 1 
            cnt += 1
        elif char_cnt[strin[e]] % 2 == 1:
            e -= 1
            cnt += 1 
        else:
            return 2 

    if cnt == 1:
        return 1 
    else:
        return 0

N = int(input())

for _ in range(N):
    strin = input().strip()
    print(isPalin(strin))
