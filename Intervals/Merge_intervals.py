from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge overlapping intervals

            - Time Complexity: O(nlogn)
            - Space Complexity: O(n)

        Args:
            intervals (List[List[int]]): List of intervals

        Returns:
            List[List[int]]: List of merged intervals
        """
        merged_intervals = []
        intervals.sort()
        previous = intervals[0]

        for current in intervals:
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged_intervals.append(previous)
                previous = current

        merged_intervals.append(previous)

        return merged_intervals
