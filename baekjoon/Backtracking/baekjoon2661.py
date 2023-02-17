N = int(input())

answer = ""


def DFS():
    global answer 

    if len(answer) == N:
        return

    for i in "123":
        answer += i 
        bad = False
        for j in range(1, N // 2 + 1): # 처음 range(N // 2) 에서 수정
            if answer[-j:] == answer[-2*j:-j]:
                bad = True 
                break
        if bad:
            answer = answer[:-1]
            continue
        DFS()
        if len(answer) == N:
            return
        answer = answer[:-1]
        

DFS()

print(answer)