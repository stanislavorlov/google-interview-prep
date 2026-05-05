# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
import sys
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        answer = []
        queue = deque([root])
        while queue:
            nodes_count = len(queue)

            max_val = -sys.maxsize
            for _ in range(nodes_count):
                node = queue.popleft()

                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(max_val)

        return answer