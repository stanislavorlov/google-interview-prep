# https://leetcode.com/problems/add-one-row-to-tree/description/?envType=daily-question&envId=2024-04-15

# Given the root of a binary tree and two integers val and depth, 
# add a row of nodes with value val at the given depth depth.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class SolutionRecursion:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            
            return node
        
        self.insert(val, root, 1, depth)

        return root

    def insert(self, val: int, node: TreeNode, depth: int, n: int):
        if node is None:
            return
        
        if depth == n - 1:
            t = node.left
            node.left = TreeNode(val)
            node.left.left = t
            t = node.right
            node.right = TreeNode(val)
            node.right.right = t
        else:
            self.insert(val, node.left, depth + 1, n)
            self.insert(val, node.right, depth + 1, n)

class Node:
    def __init__(self, node: TreeNode, d: int):
        self.node = node
        self.depth = d

class SoltuionStack:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n
        stack = deque()
        stack.append(Node(root, 1))
        while len(stack) > 0:
            n = stack.pop()
            if n.node is None:
                continue
            if n.depth == d-1:
                temp = n.node.left
                n.node.left = TreeNode(val)
                n.node.left.left = temp
                temp = n.node.right
                n.node.right = TreeNode(val)
                n.node.right.right = temp
            else:
                stack.append(Node(n.node.left, n.depth + 1))
                stack.append(Node(n.node.right, n.depth + 1))

        return root
    
tree = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
solution = SolutionRecursion()
solution.addOneRow(tree, 1, 3)