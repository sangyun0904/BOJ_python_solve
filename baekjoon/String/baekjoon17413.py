s = input()

ans = ""
tag = False
temp = ""

for i in s:
    if i == "<":
        ans += temp 
        temp=""
        tag=True 
        ans += i 
    elif i == ">":
        ans += i 
        tag=False 
    elif i == " ":
        ans += temp + " "
        temp=""
    else:
        if tag:
            ans += i 
        else:
            temp = i + temp 

print(ans + temp)