# https://leetcode.com/problems/range-sum-of-bst/

# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBSTStack(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sum = 0

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sum += node.val

            if node.left and node.left.val > low:
                stack.append(node.left)

            if node.right and node.right.val < high:
                stack.append(node.right)

        return sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        if low <= root.val <= high:
            ans += root.val

        if root.left.val > low:
            ans += self.rangeSumBST(root.left, low, high)

        if root.right.val < high:
            ans += self.rangeSumBST(root.right, low, high)

        return ans