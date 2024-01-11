from bisect import bisect_left
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        position = bisect_left(intervals, newInterval)

        print(position)


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(s.insert(intervals, newInterval))
