# Problem link : https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Returns the number of subarrays with sum equal to k

            - Time complexity: O(n)
            - Space complexity: O(n)

            - The idea is to use a dictionary to store the number of subarrays with a particular sum (prefix sum)
            till that point.

        Args:
            nums (List[int]): Input array
            k (int): Target sum

        Returns:
            int: Number of subarrays with sum equal to k
        """

        answer = 0
        prefix_dict = {0: 1}  # 1 subarray woth sum 0 (sum: number)
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_dict:
                answer += prefix_dict[prefix_sum - k]
            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

        return answer


if __name__ == "__main__":
    obj = Solution()
    print(obj.subarraySum([1, 1, 1], 2))  # 2
    print(obj.subarraySum([1, 2, 3], 3))  # 2
    print(obj.subarraySum([1, 2, 3], 5))  # 1
