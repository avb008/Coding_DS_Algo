from typing import List


class Solution:
    def disjointIntervals(self, arr: List[int], n: int) -> int:
        """Find the maximum number of disjoint intervals that can be formed from a given set of intervals

            - Time Complexity: O(nlogn)
            - Space Complexity: O(1)

        Args:
            arr (List[int]): Input intervals
            n (int): Number of intervals

        Returns:
            int: Number of disjoint intervals
        """

        disjoint_intervals = 1
        arr.sort()
        previous = arr[0]

        for current in arr[1:]:
            if current[0] <= previous[1]:
                if current[1] < previous[1]:
                    previous = current
            else:
                disjoint_intervals += 1
                previous = current

        return disjoint_intervals
