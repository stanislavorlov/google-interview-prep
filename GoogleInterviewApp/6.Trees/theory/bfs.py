# Breadth-First search

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode):
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)
        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
