def compute_min_cost(a, b, n, m, i, dp):
    if i == 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    dp[i] = float("inf")
    for j in range(1, i + 1):
        new_cost = a[j - 1] + sum(b[j - 1 : i])
        dp[i] = min(dp[i], compute_min_cost(a, b, n, m, i - j, dp) + new_cost)

    return dp[i]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [-1] * (n + 1)
    answer = compute_min_cost(a, b, n, m, n, dp)
    print(dp)
    print(answer)
