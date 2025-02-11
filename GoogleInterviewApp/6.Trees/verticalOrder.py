# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
# (i.e., from top to bottom, column by column).

from collections import defaultdict
import queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [[]]

        map = defaultdict(list)
        q = queue.Queue()
        q.put((root, 0))

        while not q.empty():
            node, level = q.get()
            map[level].append(node.val)

            if node.left:
                q.put((node.left, level - 1))

            if node.right:
                q.put((node.right, level + 1))

        return [map[x] for x in sorted(map.keys())]
    
tree = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
solution = Solution()
print(solution.verticalOrder(tree))