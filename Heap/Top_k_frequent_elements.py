# Problem : https://leetcode.com/problems/top-k-frequent-elements/description/
# Given a non-empty array of integers and an integer k, return the k most frequent elements.

# Example 1: nums = [1,1,1,2,2,3], k = 2 -> [1,2]
# Example 2: nums = [1], k = 1 -> [1]

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Find k most frequent elements in a list

            - Time complexity: O(nlogk)

        Args:
            nums (List[int]): Input list
            k (int): Input k

        Returns:
            List[int]: k most frequent elements
        """
        count = Counter(nums)
        max_heap = []
        # Time comple
        for num, freq in count.items():
            max_heap.append((-freq, num))

        heapq.heapify(max_heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])

        return ans
