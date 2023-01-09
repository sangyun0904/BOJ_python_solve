import sys 
input = sys.stdin.readline 

N = int(input())

extensions_dict = {}

for _ in range(N):
    name, ext = input().strip().split(".")
    if ext in extensions_dict:
        extensions_dict[ext] += 1 
    else:
        extensions_dict[ext] = 1 

ans = []

for k, v in extensions_dict.items():
    ans.append([k, v])

ans.sort()

for k, v in ans:
    print(k, v)