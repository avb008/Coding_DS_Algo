# Definition for a binary tree node.
# Problem : https://leetcode.com/problems/same-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Check if two binary trees are identical

        Args:
            p (Optional[TreeNode]): The root of the first binary tree
            q (Optional[TreeNode]): The root of the second binary tree

        Returns:
            bool: True if the two binary trees are identical, False otherwise
        """
        if p is None or q is None:
            return p == q

        return (
            (p.val == q.val)
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
