class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
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


if __name__ == "__main__":
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.left.right = Treenode(5)
    root.right.left = Treenode(6)
    root.right.right = Treenode(7)

    s = Solution()
    print(s.height(root))
