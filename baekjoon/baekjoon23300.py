import sys

input = sys.stdin.readline

backwards = []
forwards = []

N, Q = input().split()
cur = -1
Q = int(Q)

for i in range(Q):
    command = input().strip().split()

    if command[0] == "B":
        if len(backwards) == 0:
            continue
        else:
            forwards.append(cur)
            cur = backwards.pop()

    elif command[0] == "F":
        if len(forwards) == 0:
            continue
        else:
            backwards.append(cur)
            cur = forwards.pop()

    elif command[0] == "C":
        if len(backwards) == 0:
            continue
        page_num = backwards[-1]
        for i in range(len(backwards)-2, -1, -1):
            if backwards[i] == page_num:
                backwards.pop(i)
            else:
                page_num = backwards[i]

    else:
        forwards = []
        if cur != -1:
            backwards.append(cur)
        cur = command[1]

print(cur)
if len(backwards) == 0:
    print(-1)
else:
    for i in range(-1, -len(backwards)-1, -1):
        print(backwards[i], end=" ")
    print()
if len(forwards) == 0:
    print(-1)
else:
    for i in range(-1, -len(forwards)-1, -1):
        print(forwards[i], end=" ")
    print()
