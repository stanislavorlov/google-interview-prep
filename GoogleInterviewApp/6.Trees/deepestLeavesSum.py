# https://leetcode.com/problems/deepest-leaves-sum/
from collections import deque
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        answer = 0

        while q:
            cur_count = len(q)
            answer = 0
            for _ in range(cur_count):
                node = q.popleft()
                answer += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer

    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        next_level = deque([root])
        curr_level = deque([])

        while next_level:
            curr_level = next_level
            next_level = deque()

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        return sum([node.val for node in curr_level])