# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node.left:
                dfs(node.left)
            values.append(node.val)
            if node.right:
                dfs(node.right)

        values = []
        answer = float('inf')

        dfs(root)

        for i in range(1, len(values)):
            answer = min(answer, abs(values[i] - values[i-1]))

        return answer

    def minimumDifferenceIteractive(self, root: Optional[TreeNode]) -> int:
        stack = []
        values = []

        current = root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                values.append(current.val)
                current = current.right

        answer = float('inf')
        for i in range(1, len(values)):
            answer = min(answer, values[i] - values[i-1])

        return answer