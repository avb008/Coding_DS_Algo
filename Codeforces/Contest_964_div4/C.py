t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())

    tasks = []
    for i in range(n):
        x, y = map(int, input().split())
        tasks.append((x, y))

    tasks.sort()

    start, end = 0, 0
    bath = False
    for x, y in tasks:
        if (x - end) >= s and not bath:
            bath = True

        start = x
        end = y

    if (m - end) >= s:
        bath = True

    print("YES" if bath else "NO")
