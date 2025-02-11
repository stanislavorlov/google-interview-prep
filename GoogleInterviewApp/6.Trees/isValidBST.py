# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.

import sys
from typing import Optional

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min, max):
            if not node:
                return True
            
            if min < node.data < max:
                return dfs(node.left, min, node.data) and dfs(node.right, node.data, max)
            
            return False

        return dfs(root, -sys.maxsize, sys.maxsize)
    
solution = Solution()
tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(solution.isValidBST(tree))