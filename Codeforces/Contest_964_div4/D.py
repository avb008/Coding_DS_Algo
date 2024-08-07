t = int(input())

for _ in range(t):
    s = input()
    t = input()

    if len(t) > len(s):
        print("NO")
        continue

    modified_s = list(s)  # Start with s and modify it as needed
    s_ptr, t_ptr = 0, 0
    possible = False

    while s_ptr < len(s):
        if t_ptr < len(t) and (s[s_ptr] == t[t_ptr] or s[s_ptr] == "?"):
            modified_s[s_ptr] = t[t_ptr]
            t_ptr += 1
        elif s[s_ptr] == "?":
            modified_s[s_ptr] = "a"
        s_ptr += 1

    if t_ptr == len(t):
        possible = True

    if possible:
        print("YES")
        print("".join(modified_s))
    else:
        print("NO")
