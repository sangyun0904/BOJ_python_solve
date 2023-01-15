keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

keys_idx = {}

for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        keys_idx[keyboard[i][j]] = [i, j]

r_start, l_start = input().strip().split()

left_hand = keys_idx[r_start]
right_hand = keys_idx[l_start]

word = input().strip()

answer = 0

for i in word:
    col, row = keys_idx[i]
    if row < 4 or (col < 2 and row == 4):
        answer += abs(col - left_hand[0])
        answer += abs(row - left_hand[1])
        left_hand = [col, row]
    else:
        answer += abs(col - right_hand[0])
        answer += abs(row - right_hand[1])
        right_hand = [col, row]

    answer += 1 

print(answer)