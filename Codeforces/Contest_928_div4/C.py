def digit_sum(n):
    return sum(int(x) for x in str(n))


total_sum = [0] * 200005
for i in range(1, 200005):
    total_sum[i] = total_sum[i - 1] + digit_sum(i)

t = int(input())
for _ in range(t):
    n = int(input())
    print(total_sum[n])
