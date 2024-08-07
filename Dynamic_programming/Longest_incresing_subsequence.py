from typing import List

class Solution:

    def lengthofLIS_brute_force(self, nums: List[int]) -> int:
        # Time Complexity: O(2^n)
        # Space Complexity: O(n) - recursion stack

        if len(nums) == 0:
            return 0
        def traverse(nums, index, prev):
            if index == len(nums):
                return 0
            taken = 0
            if nums[index] > prev: # taken 
                taken = 1 + traverse(nums, index+1, nums[index])
            not_taken = traverse(nums, index+1, prev) # not taken
            return max(taken, not_taken) # return the max of taken and not taken
        
        return traverse(nums, 0, float('-inf'))

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
    
    def printLIS(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        dp = [1] * len(nums)
        # dp[i] = length of LIS ending at index i
        # dp[i] = max(dp[j]) + 1 for all j < i and nums[j] < nums[i]
        # dp[i] = 1 if there is no such j
        # Finding the LIS is equivalent to finding the max(dp[i]) for all i
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j]+1)

        print(dp)
        max_len = max(dp)
        res = []
        for i in range(len(dp)-1, -1, -1):
            if dp[i] == max_len: # found the last element of LIS
                res.append(nums[i]) # append it to the result
                max_len -= 1 # decrement max_len
        return res[::-1] # reverse the result
    

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(nums)
    print(s.lengthOfLIS(nums))
    print(s.lengthofLIS_brute_force(nums))
    print(s.printLIS(nums))