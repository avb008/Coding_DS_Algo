t = int(input())


def compute_wins(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())

    wins = 0
    if compute_wins(a1, b1) + compute_wins(a2, b2) > 0:
        wins += 1
    if compute_wins(a1, b2) + compute_wins(a2, b1) > 0:
        wins += 1
    if compute_wins(a2, b1) + compute_wins(a1, b2) > 0:
        wins += 1
    if compute_wins(a2, b2) + compute_wins(a1, b1) > 0:
        wins += 1

    print(wins)
