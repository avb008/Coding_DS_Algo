t = int(input())
for _ in range(t):
    n = int(input())
    houses = input()
    total_zeroes = houses.count("0")
    total_ones = n - total_zeroes
    left_zeroes, left_ones = 0, 0
    right_zeroes, right_ones = total_zeroes, total_ones

    ans = -1
    diff = float("inf")
    if right_ones >= n / 2:
        ans = 0
        diff = n // 2 - ans
    for i in range(n):
        if houses[i] == "0":
            left_zeroes += 1
            right_zeroes -= 1
        else:
            left_ones += 1
            right_ones -= 1

        if right_ones >= (n - i - 1) / 2 and left_zeroes >= (i + 1) / 2:
            new_diff = abs(n / 2 - i - 1)
            if new_diff < diff:
                diff = new_diff
                ans = i + 1
    print(ans)
