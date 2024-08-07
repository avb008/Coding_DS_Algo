t = int(input())
for _ in range(t):
    a, b, m = map(int, input().split())

    answer = m // a + 2 + m // b
    print(answer)
