# Balanced Binary Tree : For every node , height(left) - height(right) <= 1
# Problem: https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def height(self, current_node) -> int:
        """Calculate height of a binary tree

            - Time Complexity: O(n)
            - Space Complexity: O(n)

            - Formula: height = max(left_height, right_height) + 1

        Args:
            current_node (_type_): Current node of the binary tree

        Returns:
            int: Height of the binary tree
        """
        if current_node is None:
            return 0

        left = self.height(current_node.left)
        right = self.height(current_node.right)

        height = max(left, right) + 1

        return height

    def bruteforce_checkForBalancedBinaryTree(self, root: Optional[Treenode]) -> bool:
        """Check if a binary tree is balanced or not

            - Time Complexity: O(n^2) (n^2 because for every node we are calculating height of left and right subtree)
            - Space Complexity: O(n)

        Args:
            root (Optional[Treenode]): Root node of the binary tree

        Returns:
            bool: True if balanced, False otherwise
        """

        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if (
            abs(left_height - right_height) <= 1
            and self.bruteforce_checkForBalancedBinaryTree(root.left)
            and self.bruteforce_checkForBalancedBinaryTree(root.right)
        ):
            return True

        return False

    def checkForBalancedBinaryTree(self, root: Optional[Treenode]) -> bool:
        """Check if a binary tree is balanced or not

            - Time Complexity: O(n)
            - Space Complexity: O(n)

        Args:
            root (Optional[Treenode]): Root node of the binary tree

        Returns:
            bool: True if balanced, False otherwise
        """

        if root is None:
            return True

        def traverse(current_node) -> int:
            """Traverse the binary tree and calculate height of left and right subtree and check if the difference
            is greater than 1 or not. If it is greater than 1 then return -1 else return height of the subtree

                - Time Complexity: O(n)
                - Space Complexity: O(n)

            Args:
                current_node (_type_): Current node of the binary tree

            Returns:
                int: Height of the binary tree
            """
            if current_node is None:
                return 0

            left_height = traverse(current_node.left)
            right_height = traverse(current_node.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            height = max(left_height, right_height) + 1

            return height

        return traverse(root) != -1
