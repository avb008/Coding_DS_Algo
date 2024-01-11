from typing import List


class Solution:
    def recurPermute(
        self, nums: List[int], ds: List[int], ans: List[List[int]], freq: List[bool]
    ) -> None:
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return

        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                ds.append(nums[i])
                self.recurPermute(nums, ds, ans, freq)
                freq[i] = False
                ds.pop()

    def permuteBF(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []
        freq = [False] * len(nums)
        self.recurPermute(nums, ds, ans, freq)

        return ans
