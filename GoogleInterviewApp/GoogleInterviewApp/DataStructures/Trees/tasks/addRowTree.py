# https://leetcode.com/problems/add-one-row-to-tree/description/?envType=daily-question&envId=2024-04-15

# Given the root of a binary tree and two integers val and depth, 
# add a row of nodes with value val at the given depth depth.

from queue import Queue
from typing import Optional

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = Queue()
        queue.put(root)

        height = 1

        while not queue.empty() and height < depth:
            node = queue.get()

            if node.left:
                queue.put(node.left)

            if node.right:
                queue.put(node.right)

            depth -= 1

        # get all nodes from queue and create child