# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])

    def traverse(self, root: Optional[TreeNode], nodes: list) -> list[int]:
        if not root:
            return nodes

        if root.left:
            self.traverse(root.left, nodes)

        nodes.append(root.val)

        if root.right:
            self.traverse(root.right, nodes)

        return nodes