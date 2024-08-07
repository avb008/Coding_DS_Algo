t = int(input())
for _ in range(t):
    s = input()
    if len(set(s)) == 1:
        print("NO")
    else:
        print("YES")
        if s[::-1] == s:
            mid = len(s) // 2
            print(s[mid] + s[:mid] + s[mid + 1 :])
        else:
            print(s[::-1])
