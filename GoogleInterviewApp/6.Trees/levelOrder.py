# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Given the root of a binary tree, return the level order traversal of its nodes' values.

from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    
    result = defaultdict(list)
    queue = deque()
    queue.append((root, 0))
    while queue:
        (node, level) = queue.popleft()
        result[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return list(result.values())

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(levelOrder(None, tree))