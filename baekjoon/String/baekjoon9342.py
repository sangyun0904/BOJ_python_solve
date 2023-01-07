import sys 
input = sys.stdin.readline

rule = ['A', 'F', 'C']

def isInfected(gene):

    if gene[0] != rule[0]:
        if gene[0] not in ['B', 'C', 'D', 'E', 'F']:
            return "Good"
        else:
            gene = gene[1:]
    
    if gene[-1] != rule[-1]:
        if gene[-1] not in ['B', 'C', 'D', 'E', 'F']:
            return "Good"
        else:
            gene = gene[:-1]

    idx_g = 0
    idx_r = 0

    while idx_r < 3 and idx_g < len(gene):
        if gene[idx_g] == rule[idx_r]:
            idx_g += 1 
        else:
            idx_r += 1 

    if idx_r == 3:
        return "Good"
    return "Infected!"

    

T = int(input())
for _ in range(T):
    gene = input().strip()
    print(isInfected(gene))