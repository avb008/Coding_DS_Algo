# Problem: Lowest common ancestor of a binary tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """Find Lowest Common Ancestor of a Binary Tree

            - Time Complexity: O(n)
            - Space Complexity: O(n)

            - Algorithm:
                - If root is None or root is either of the given nodes, return root
                - Recursively call the function on left and right subtree
                - If left is None, return right
                - If right is None, return left
                - Else return root

        Args:
            root (TreeNode): Root of the tree
            p (TreeNode): Treenode of 1st node
            q (TreeNode): Treenode of 2nd node

        Returns:
            TreeNode: Lowest Common Ancestor of the given 2 nodes
        """

        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # If p and q are on both sides
        return (
            left if left else right
        )  # Either one of p,q is on one side OR p,q is not in L&R subtrees


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    sol = Solution()

    print(sol.lowestCommonAncestor(root, root.left, root.right).val)
