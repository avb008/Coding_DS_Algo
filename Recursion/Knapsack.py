class Solution:
    def computeMax(self, index, W, wt, val) -> int:
        """Compute max value that can be put in knapsack of capacity W

            - Time complexity: O(2^n)
            - Space complexity: O(1)
        Args:
            index (_type_): Index of the item
            W (_type_): Max weight of the knapsack
            wt (_type_): List of weights of the items
            val (_type_): List of values of the items

        Returns:
            int: Max value that can be put in knapsack of capacity W
        """
        if index == 0:
            if wt[index] <= W:
                return val[index]
            return 0

        # pick
        pick = float("-inf")
        if wt[index] <= W:
            pick = val[index] + self.computeMax(index - 1, W - wt[index], wt, val)

        non_pick = self.computeMax(index - 1, W, wt, val)

        return max(pick, non_pick)

    def knapSack01BruteForce(self, W, wt, val, n):
        return self.computeMax(n - 1, W, wt, val)

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack01(self, W, wt, val, n):
        max_value = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for index in range(n):
            for weight in range(W + 1):
                if index == 0:
                    if wt[index] <= weight:
                        max_value[index][weight] = val[index]
                    continue

                # pick
                pick = float("-inf")
                if wt[index] <= weight:
                    pick = val[index] + max_value[index - 1][weight - wt[index]]

                non_pick = max_value[index - 1][weight]

                max_value[index][weight] = max(pick, non_pick)

        return max_value[n - 1][W]


if __name__ == "__main__":
    obj = Solution()
    print(obj.knapSack01BruteForce(4, [4, 5, 1], [1, 2, 3], 3))  # 3
    print(obj.knapSack01(4, [4, 5, 1], [1, 2, 3], 3))  # 3
    print(obj.knapSack01BruteForce(5, [1, 2, 3], [10, 15, 40], 3))  # 55
    print(obj.knapSack01(5, [1, 2, 3], [10, 15, 40], 3))  # 55
    print(obj.knapSack01BruteForce(3, [1, 2, 3], [10, 15, 40], 3))  # 40
    print(obj.knapSack01(3, [1, 2, 3], [10, 15, 40], 3))  # 40
