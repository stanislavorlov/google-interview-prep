from queue import Queue
from collections import deque

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode):
    queue = Queue()
    queue.put(root)
    while queue:
        node = queue.get()
        print(node.val)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)

def dfs(root: TreeNode):
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

#           5
#       4           8
#   11         13        4
# 7    2              5     1
#bfs(root)
dfs(root)