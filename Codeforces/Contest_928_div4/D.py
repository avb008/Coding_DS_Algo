import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    nums = list(map(int, sys.stdin.readline().split()))
    nums_counter = {}
    number_of_groups = 0

    for i in nums:
        if i in nums_counter:
            nums_counter[i] += 1
        else:
            nums_counter[i] = 1
        complement = 2147483647 - i
        if complement in nums_counter and nums_counter[complement] > 0:
            nums_counter[complement] -= 1
            nums_counter[i] -= 1
        else:
            number_of_groups += 1

    print(number_of_groups)
