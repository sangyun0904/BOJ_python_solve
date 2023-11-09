import sys

input = sys.stdin.readline

pitch_type = ["", "ball", "hit", "wild"]
base = [False for i in range(4)]
score = 0
ball_cnt = 0

N = int(input())
pitcher_balls = list(map(int, input().split()))


def ball_4():
    global ball_cnt, score

    if base[3] and base[2] and base[1]:
        score += 1
    elif base[2] and base[1]:
        base[3] = True
    elif base[1]:
        base[2] = True
    else:
        base[1] = True
    ball_cnt = 0


for i in pitcher_balls:

    if pitch_type[i] == "ball":
        ball_cnt += 1

        if ball_cnt == 4:
            ball_4()

    if pitch_type[i] == "hit":
        ball_4()

    if pitch_type[i] == "wild":
        if base[3]:
            score += 1
            base[3] = False
        if base[2]:
            base[3] = True
            base[2] = False
        if base[1]:
            base[2] = True
            base[1] = False

        ball_cnt += 1

        if ball_cnt == 4:
            ball_4()

print(score)
