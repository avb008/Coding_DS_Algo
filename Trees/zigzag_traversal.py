# Problem : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Zigzag level order traversal of a binary tree

            - Time complexity: O(n)
            - Space complexity: O(n)

            - This is a variant of the level order traversal problem. The only difference is that the nodes at even
            levels are traversed from left to right and the nodes at odd levels are traversed from right to left.
            - We can use a queue to store the nodes at each level. We can use a flag to indicate whether the nodes at
            the current level should be traversed from left to right or from right to left.

        Args:
            root (Optional[TreeNode]): Root of the binary tree

        Returns:
            List[List[int]]: Zigzag level order traversal of the binary tree
        """
        if root is None:
            return []

        zigzag_traversal = []
        queue = deque([root])
        level = 0
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                current_node = queue.popleft()
                temp.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            if level % 2 == 1:
                zigzag_traversal.append(temp[::-1])
            else:
                zigzag_traversal.append(temp)
            level += 1

        return zigzag_traversal
