import sys 
input = sys.stdin.readline 

def isPalin(word):
    left = 0 
    right = len(word)-1 
    while right > left :
        if word[left] == word[right]:
            left += 1 
            right -= 1 
        else:
            if isSimilarPalin(left+1, right, word) or isSimilarPalin(left, right-1, word):
                return 1
            return 2 

    return 0


def isSimilarPalin(left, right, word):
    while right > left:
        if word[left] == word[right]:
            left += 1 
            right -= 1 
        else:
            return False
    return True


N = int(input())

for _ in range(N):
    word = input().strip()
    print(isPalin(word))
