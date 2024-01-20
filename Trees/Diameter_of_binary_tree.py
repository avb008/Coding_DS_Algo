# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root

# Problem : https://leetcode.com/problems/diameter-of-binary-tree/


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def ComputeDiameter(self, current_node, diameter) -> int:
        """Compute diameter of a binary tree

        Args:
            current_node (_type_): Current node of the binary tree
            diameter (_type_): Diameter of the binary tree

        Returns:
            int: Diameter of the binary tree
        """

        if current_node is None:
            return 0

        def height(current_node, diameter):
            if current_node is None:
                return 0
            left_height = height(current_node.left, diameter)
            right_height = height(current_node.right, diameter)

            diameter[0] = max(diameter[0], left_height + right_height)

            return max(left_height, right_height) + 1

        diameter = [0]
        height(self.root, diameter)

        return diameter[0]


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Treenode(1)
    bt.root.left = Treenode(2)
    bt.root.right = Treenode(3)
    bt.root.right.left = Treenode(4)
    bt.root.right.left.left = Treenode(5)
    bt.root.right.left.left.left = Treenode(6)
    bt.root.right.right = Treenode(7)
    bt.root.right.right.right = Treenode(8)
    bt.root.right.right.right.right = Treenode(9)

    diameter = [0]

    print(
        f"Diameter of the binary tree computed using recursion : {bt.ComputeDiameter(bt.root, diameter)}"
    )
