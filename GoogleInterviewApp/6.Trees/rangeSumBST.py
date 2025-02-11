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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sum = 0

        while len(stack):
            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    sum += node.val

                if node.val >= low:
                    stack.append(node.left)

                if node.val <= high:
                    stack.append(node.right)

        return sum