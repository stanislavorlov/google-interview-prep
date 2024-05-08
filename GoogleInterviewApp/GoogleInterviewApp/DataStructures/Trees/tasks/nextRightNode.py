# You are given a perfect binary tree (each node has 2 children)
# Populate each next pointer to point to its next right node.

from collections import deque
from queue import Queue
from typing import Optional

class Node:
    def __init__(self, val: int, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#                   1
#           2               3
#       4       4       6       7
#
#                  | |
#                   ↓
#
#                   1   -> Null
#               2   ->  3   -> Null
#           4 -> 5  -> 6 -> 7   -> Null
#
#

class LevelNode:
    def __init__(self, node: Node, level: int) -> None:
        self.node = node
        self.level = level

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        queue = Queue()
        queue.put(LevelNode(root, 1))

        prevNode = None
        while not queue.empty():
            levelNode = queue.get()
            node = levelNode.node
            if prevNode and prevNode.level == levelNode.level:
                prevNode.node.next = levelNode.node
            if node.left:
                queue.put(LevelNode(node.left, levelNode.level + 1))
            if node.right:
                queue.put(LevelNode(node.right, levelNode.level + 1))
            prevNode = levelNode

        return root
    
    def connect2(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        
        q = deque([root])
        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()

                if i < size - 1:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root

solution = Solution()
tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
solution.connect2(tree)