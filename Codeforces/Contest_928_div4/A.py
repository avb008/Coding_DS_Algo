t = int(input())

for _ in range(t):

    s = input()
    count = 0
    for i in s:
        if i == "A":
            count += 1

    if count >= 3:
        print("A")
    else:
        print("B")
