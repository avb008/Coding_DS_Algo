t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    r, b, flag = 0, 0, False
    for i in range(1, 13):
        if i == a or i == b:
            r += 1
        else:
            b += 1

        if abs(r - b) > 1:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")
