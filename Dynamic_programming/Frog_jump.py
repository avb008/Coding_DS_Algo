from typing import List


class Solution:
    def frogJump(n: int, heights: List[int]) -> int:
        # Write your code here.
        energy = [0] * (n + 1)

        for i in range(1, n):
            step1 = abs(heights[i] - heights[i - 1])
            step2 = float("inf")
            if i > 1:
                step1 = abs(heights[i] - heights[i - 1]) + energy[i - 1]
                step2 = abs(heights[i] - heights[i - 2]) + energy[i - 2]
            energy[i] = min(step1, step2)

        return energy[n - 1]
