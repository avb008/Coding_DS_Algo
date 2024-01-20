from collections import deque


class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def BFS(self, current_node) -> None:
        """Breadth First Search

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            current_node (_type_): Current node
        """
        if current_node is None:
            return

        queue = deque([current_node])
        while queue:
            current_node = queue.popleft()

            print(current_node.val, end=" ")

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        print()

    def preorder(self, current_node) -> None:
        """Preorder traversal (DFS)

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            current_node (_type_): Current node
        """
        if current_node is None:
            return

        print(current_node.val, end=" ")
        self.preorder(current_node.left)
        self.preorder(current_node.right)

    def inorder(self, current_node) -> None:
        """Inorder traversal (DFS)

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            current_node (_type_): Current node
        """

        if current_node is None:
            return

        self.inorder(current_node.left)
        print(current_node.val, end=" ")
        self.inorder(current_node.right)

    def postorder(self, current_node):
        """Postorder traversal (DFS)

            - Time complexity: O(n)
            - Space complexity: O(n)

        Args:
            current_node (_type_): Current node
        """
        if current_node is None:
            return

        self.postorder(current_node.left)
        self.postorder(current_node.right)
        print(current_node.val, end=" ")
