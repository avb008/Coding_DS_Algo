# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Problem  : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from typing import Optional, List


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def maxPathSum(self, root: Optional[Treenode]) -> int:
        """Compute the maximum path sum of a binary tree

            - Time complexity: O(n)
            - Space complexity: O(n)

            - This is a variant of the diameter of a binary tree problem. The only difference is that the path may or
            may not pass through the root.
            - The maximum path sum is the maximum of the following:
                - The maximum path sum of the left subtree
                - The maximum path sum of the right subtree
                - The sum of the left subtree, right subtree and the root node

        Args:
            root (Optional[Treenode]): Root of the binary tree

        Returns:
            int: Maximum path sum of the binary tree
        """

        if root is None:
            return 0

        def maxPathSumUtil(root: Optional[Treenode], maxSum: List[int]) -> int:
            if root is None:
                return 0

            left = maxPathSumUtil(root.left, maxSum)
            right = maxPathSumUtil(root.right, maxSum)

            maxSum[0] = max(maxSum[0], left + right + root.val)

            return max(left, right) + root.val

        max_path_sum = [float("-inf")]
        maxPathSumUtil(root, max_path_sum)

        return max_path_sum[0]
