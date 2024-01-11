# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Dict, List, Optional


class Solution:
    def inorder(
        self,
        root: Optional[TreeNode],
        all_trees: Dict,
        identical_subtrees: List[Optional[TreeNode]],
    ) -> str:
        """Inorder traversal of the binary tree to find the duplicate subtrees

            - Time Complexity: O(n^2) where n is the number of nodes in the binary tree
            - Space Complexity: O(n^2) where n is the number of nodes in the binary tree

            All the subtrees are stored in a dictionary. If the subtree is already present
            in the dictionary, then it is a duplicate subtree. The dictionary stores the
            subtree representation as the key and the number of times the subtree is
            present as the value.

        Args:
            root (Optional[TreeNode]): Node of the binary tree
            all_trees (Dict): Dictionary to store the representation of all the subtrees
            identical_subtrees (List[Optional[TreeNode]]): List of duplicate subtrees

        Returns:
            str: Representation of the subtree
        """

        if root is None:
            return ""

        tree_rep = "("
        tree_rep += self.inorder(root.left, all_trees, identical_subtrees)
        tree_rep += str(root.val)
        tree_rep += self.inorder(root.right, all_trees, identical_subtrees)
        tree_rep += ")"

        if tree_rep in all_trees and all_trees[tree_rep] == 1:
            identical_subtrees.append(root)

        all_trees[tree_rep] = all_trees.get(tree_rep, 0) + 1

        return tree_rep

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        """Finds the duplicate subtrees in a binary tree. A binary tree is a duplicate
            subtree if there are two subtrees of the binary tree that have the same
            structure and the same node values.

            - Time Complexity: O(n^2) where n is the number of nodes in the binary tree
            - Space Complexity: O(n^2) where n is the number of nodes in the binary tree

        Args:
            root (Optional[TreeNode]): Root of the binary tree

        Returns:
            List[Optional[TreeNode]]: List of duplicate subtrees
        """

        all_trees, identical_subtrees = {}, []

        self.inorder(root, all_trees, identical_subtrees)

        return identical_subtrees
