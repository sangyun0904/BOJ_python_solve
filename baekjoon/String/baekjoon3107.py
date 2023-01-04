def ipv6(s):
    ret = ""
    ip = s.split(":")
    if s == "::":
        ret = "0000:" * 8
    elif ip[0] == "":
        ip = ip[2:]
        ret += "0000:" * (8 - len(ip))
        for i in ip:
            ret += "0"*(4-len(i)) + i + ":"
    elif ip[-1] == "":
        ip = ip[:-2]
        for i in ip:
            ret += "0"*(4-len(i)) + i + ":"
        ret += "0000:" * (8 - len(ip))
    else:
        for i in ip:
            if i == "":
                ret += "0000:" * (8 - len(ip) + 1)
            else:
                ret += "0"*(4-len(i)) + i + ":"
    
    return ret[:-1]

print(ipv6(input()))