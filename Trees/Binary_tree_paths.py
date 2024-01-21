# Problem : https://leetcode.com/problems/binary-tree-paths/description/
# Given a binary tree, return all root-to-leaf paths.

from typing import Optional, List


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def binaryTreePaths(self, root: Optional[Treenode]) -> List[str]:
        """Return all Binary tree paths

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            root (Optional[Treenode]): Root of the binary tree

        Returns:
            List[str]: List of all binary tree paths
        """
        paths = []
        if root is None:
            return paths

        def dfs(
            current_node: Optional[Treenode], current_path: str, paths: List[str]
        ) -> None:
            if current_node.left is None and current_node.right is None:
                paths.append(current_path + str(current_node.val))
                return

            current_path += str(current_node.val) + "->"

            if current_node.left:
                dfs(current_node.left, current_path, paths)
            if current_node.right:
                dfs(current_node.right, current_path, paths)

        dfs(root, "", paths)

        return paths


if __name__ == "__main__":
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.right = Treenode(5)
    root.left.left = Treenode(4)
    root.right.right = Treenode(6)
    root.right.left = Treenode(7)

    binary_tree = BinaryTree()
    print(binary_tree.binaryTreePaths(root))  # ["1->2->5", "1->3"]
