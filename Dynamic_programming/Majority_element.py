# Problem : https://leetcode.com/problems/majority-element/
# Find the majority element in an array of size n where majority element occurs more than n/2 times

from typing import List


class Solution:
    def majorityElement_v1(self, nums: List[int]) -> int:
        """Find the majority element in an array of size n where majority element occurs more than n/2 times

            - Time Complexity: O(n)
            - Space Complexity: O(n)

            - Algorithm:
                - Create a dictionary to store the count of each element
                - Return the element with count > n/2

        Args:
            nums (List[int]): List of integers

        Returns:
            int: Majority element
        """

        count_dict = {}
        for i in nums:
            count_dict[i] = count_dict.get(i, 0) + 1

        for k, v in count_dict.items():
            if v > len(nums) // 2:
                return k

    def majorityElement_v2(self, nums: List[int]) -> int:
        """Find the majority element in an array of size n where majority element occurs more than n/2 times

            - Time Complexity: O(n)
            - Space Complexity: O(1)

            - Algorithm:
                - Moore's voting algorithm
                - Initialize the count to 0 and candidate to None
                - For each element in the array:
                    - If count is 0, assign the current element as candidate
                    - If current element is same as candidate, increment the count
                    - Else decrement the count
                - Return the candidate

        Args:
            nums (List[int]): List of integers

        Returns:
            int: Majority element
        """

        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if i == candidate else -1

        count = sum(1 for i in nums if i == candidate)

        return candidate if count > len(nums) // 2 else -1

    def majorityElement_n3(self, nums: List[int]) -> List[int]:
        """Return Majority elements that occur more than [n//3] times .

            - Time Complexity: O(n)
            - Space Complexity: O(1)

            - Algorithm:
                - Moore's voting algorithm
                - Initialize the count1, count2 to 0 and candidate1, candidate2 to None
                - For each element in the array:
                    - If count1 is 0, assign the current element as candidate1
                    - If count2 is 0, assign the current element as candidate2
                    - If current element is same as candidate1, increment the count1
                    - If current element is same as candidate2, increment the count2
                    - Else decrement the count1 and count2
                - Return the candidate1, candidate2

            - Note: There can be at most 2 majority elements that occur more than [n//3] times
            - Edge cases : [2,1,1,3,1,4,5,6]

        Args:
            nums (List[int]): Input array

        Returns:
            List[int]: List of majority elements
        """

        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        for num in nums:
            if count1 == 0 and num != candidate2:
                candidate1 = num
                count1 += 1
            elif count2 == 0 and num != candidate1:
                candidate2 = num
                count2 += 1
            elif num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = sum(1 for i in nums if i == candidate1)
        count2 = sum(1 for i in nums if i == candidate2)

        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement_v1(nums))
    print(s.majorityElement_v2(nums))

    nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    print(s.majorityElement_n3(nums))
    nums = [2, 1, 1, 3, 1, 4, 1, 6]
    print(s.majorityElement_n3(nums))
