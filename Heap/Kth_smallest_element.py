from typing import List
import heapq


class Solution:
    def findKthSmallestMinHeap(self, nums: List[int], k: int) -> int:
        """Find kth smallest element in a list using min heap

            - Time complexity: O(n + klogn)
            - Space complexity: O(n) for heap

        Args:
            nums (List[int]): Input list
            k (int): Input k

        Returns:
            int: kth smallest element
        """
        heapq.heapify(nums)  # O(n)
        for i in range(k):
            ans = heapq.heappop(nums)  # O(logn)
            if i == k - 1:
                return ans

    def findKthSmallestMaxHeap(self, nums: List[int], k: int) -> int:
        """Find kth smallest element in a list using max heap

            - Time complexity: O(nlogk)
            - Space complexity: O(k) for heap

        Args:
            nums (List[int]): Input list
            k (int): Input k

        Returns:
            int: kth smallest element
        """

        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return -max_heap[0]
