from math import ceil

t = int(input())

for _ in range(t):
    intro, extra, univ = map(int, input().split())
    total = intro
    total += extra // 3
    remaining = extra % 3

    if remaining and remaining + univ < 3:
        print(-1)
    else:
        total += ceil((remaining + univ) / 3)
        print(total)
