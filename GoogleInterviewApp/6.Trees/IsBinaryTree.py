# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

# The data value of every node in a node's left subtree is less than the data value of that node.
# The data value of every node in a node's right subtree is greater than the data value of that node.
# The data value of every node is distinct.

import sys

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root: node):
    return checkNode(root, -sys.maxsize - 1, sys.maxsize)

def checkNode(node: node, min: int, max: int):
    if not node:
        return True
    
    if node.data < min or node.data > max:
        return False
    
    return checkNode(node.left, min, node.data-1) and checkNode(node.right, node.data+1, max)