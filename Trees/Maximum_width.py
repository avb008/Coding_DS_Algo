# Maximum number of nodes at any level in between two nodes a binary tree

from typing import Optional
from collections import deque


class Treenode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def max_width(self, root: Optional[Treenode]) -> int:
        """Calculates the maximum width of a binary tree

            - Time complexity: O(n)
            - Space complexity: O(n)

            - Algorithm:
                - Use BFS to traverse the tree
                - For each level, calculate the width of the level (Assign index to each node based on its position in the level)
                - For each level, keep track of the minimum and maximum index of the nodes
                - Width of the level = maximum index - minimum index + 1

        Args:
            root (Optional[Treenode]): Root node of a binary tree

        Returns:
            int: Maximum width of a binary tree
        """
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_nodes = len(queue)

            min_pos = queue[0][1]
            for i in range(level_nodes):
                node, pos = queue.popleft()
                cur_pos = pos - min_pos

                if i == 0:
                    level_min = cur_pos
                if i == level_nodes - 1:
                    level_max = cur_pos

                if node.left:
                    queue.append((node.left, pos * 2 + 1))
                if node.right:
                    queue.append((node.right, pos * 2 + 2))

            max_width = max(max_width, level_max - level_min + 1)

        return max_width


if __name__ == "__main__":
    root = Treenode(1)

    root.left = Treenode(2)
    root.right = Treenode(3)

    root.left.left = Treenode(4)
    root.left.left.left = Treenode(5)

    root.right.right = Treenode(8)
    root.right.right.right = Treenode(7)

    sol = Solution()
    print(sol.max_width(root))
