# Given a binary tree, find its minimum depth.

# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

import sys
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root, depth = 1):
            nonlocal min_depth
            if root.left:
                dfs(root.left, depth + 1)

            if root.right:
                dfs(root.right, depth + 1)

            if not root.left and not root.right and depth < min_depth:
                min_depth = depth

        min_depth = sys.maxsize
        dfs(root)

        return min_depth

sol = Solution()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.minDepth(tree))

tree = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(sol.minDepth(tree))