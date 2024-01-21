from typing import List
import bisect


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

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """Insert new interval into a list of intervals and merge them if necessary to get a list of non-overlapping intervals

            - Time Complexity: O(nlogn)
            - Space Complexity: O(n)

        Args:
            intervals (List[List[int]]): List of intervals
            newInterval (List[int]): New interval to be inserted

        Returns:
            List[List[int]]: List of merged non-overlapping intervals
        """
        if len(intervals) == 0:
            return [newInterval]

        insert_index = bisect.bisect_left(intervals, newInterval)
        combined_intervals = []
        combined_intervals.extend(intervals[:insert_index])
        combined_intervals.append(newInterval)
        combined_intervals.extend(intervals[insert_index:])

        return self.merge(combined_intervals)


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
