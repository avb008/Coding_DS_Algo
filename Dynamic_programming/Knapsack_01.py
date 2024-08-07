from typing import List


class Solution:
    def knapsack(
        self, weights: List[int], profits: List[int], bag_limit: int, index: int
    ) -> int:
        """Knapsack 0/1 problem

                - Time Complexity: O(2^n)
                        - Space Complexity: O(n)

        Args:
                        weights (List[int]): Item weights
                        profits (List[int]): Item profits
                        bag_limit (int): Bag limit
                        index (int): Index of item

        Returns:
                        int: Maximum profit
        """

        if index == 0:
            if weights[0] <= bag_limit:
                return profits[0]
            return 0

        steal = (
            profits[index]
            + self.knapsack(weights, profits, bag_limit - weights[index], index - 1)
            if weights[index] <= bag_limit
            else float("-inf")
        )
        dont_steal = self.knapsack(weights, profits, bag_limit, index - 1)

        return max(steal, dont_steal)

    def knapsackMemoization(
        self,
        weights: List[int],
        profits: List[int],
        bag_limit: int,
        index: int,
        max_profit: List[List[int]],
    ) -> int:
        """Knapsack 0/1 problem using memoization

                - Time Complexity: O(n*bag_limit)
                - Space Complexity: O(n*bag_limit)

        Args:
                weights (List[int]): Item weights
                profits (List[int]): Item profits
                bag_limit (int): Bag limit
                index (int): Index of item
                max_profits (List[List[int]]): Memoization array

        Returns:
                int: Maximum profit
        """

        if index == 0:
            if weights[0] <= bag_limit:
                return profits[0]
            return 0

        if max_profit[index][bag_limit]:
            return max_profit[index][bag_limit]

        steal = (
            profits[index]
            + self.knapsackMemoization(
                weights, profits, bag_limit - weights[index], index - 1, max_profit
            )
            if weights[index] <= bag_limit
            else float("-inf")
        )
        dont_steal = self.knapsackMemoization(
            weights, profits, bag_limit, index - 1, max_profit
        )

        max_profit[index][bag_limit] = max(steal, dont_steal)

        return max_profit[index][bag_limit]


if __name__ == "__main__":
    profits = [1, 6, 10, 16]
    weights = [1, 2, 3, 5]
    bag_limit = 7
    obj = Solution()

    # ----------------------------------------- Recursive -----------------------------------------#
    print(obj.knapsack(weights, profits, bag_limit, len(weights) - 1))

    # ----------------------------------------- Memoization -----------------------------------------#
    n = len(weights)
    max_profit = [[None for _ in range(bag_limit + 1)] for _ in range(n)]
    max_profit[0][0] = profits[0] if weights[0] <= bag_limit else 0
    obj.knapsackMemoization(weights, profits, bag_limit, len(weights) - 1, max_profit)
    print(max_profit[n - 1][bag_limit])

    # ----------------------------------------- Bottom Up DP -----------------------------------------#
    # DP using 2D array
    profits_dp = [[0 for _ in range(bag_limit + 1)] for _ in range(n)]
    for weight in range(weights[0], bag_limit + 1):
        profits_dp[0][weight] = profits[0]

    for index in range(n):
        for bag_size in range(bag_limit + 1):
            if weights[index] <= bag_size:
                profits_dp[index][bag_size] = (
                    profits[index] + profits_dp[index][bag_size - weights[index]]
                )

            profits_dp[index][bag_size] = max(
                profits_dp[index][bag_size], profits_dp[index - 1][bag_size]
            )

    print(profits_dp[n - 1][bag_limit])

    # ----------------------------------------- Space Optimized DP using 2 arrays -----------------------------------------#
    previous = [0 for _ in range(bag_limit + 1)]
    current = [0 for _ in range(bag_limit + 1)]
    for weight in range(weights[0], bag_limit + 1):
        previous[weight] = profits[0]

    for index in range(1, n):
        for bag_size in range(bag_limit + 1):
            if weights[index] <= bag_size:
                current[bag_size] = max(
                    current[bag_size],
                    profits[index] + previous[bag_size - weights[index]],
                )
            current[bag_size] = max(current[bag_size], previous[bag_size])

        previous = current

    print(current[bag_limit])
