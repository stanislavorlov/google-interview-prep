# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if root.left == None or root.right == None:
            return False
        
        arr_left = []
        self.in_order(root.left, arr_left)
        arr_right = []
        self.post_order(root.right, arr_right)

        return arr_left == arr_right

    def in_order(self, tree: TreeNode, arr = []):
        if tree.left:
            self.in_order(tree.left, arr)
        arr.append(tree.val)
        if tree.right:
            self.in_order(tree.right, arr)

    def post_order(self, tree: TreeNode, arr = []):
        if tree.right:
            self.post_order(tree.right, arr)
        arr.append(tree.val)
        if tree.left:
            self.post_order(tree.left, arr)
        
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
        if not tree1 and not tree2:
            return True
        if tree1 == None or tree2 == None:
            return False
        return tree1.val == tree2.val and self.is_mirror(tree1.left, tree2.right) and self.is_mirror(tree1.right, tree2.left)
    
def is_symmetric(root):
    return is_mirror(root, root)

def is_mirror(tree1, tree2) -> bool:
    if not tree1 and not tree2:
        return True
    
    if not tree1 or not tree2:
        return False
    
    return tree1.val == tree2.val and is_mirror(tree1.left, tree2.right) and is_mirror(tree1.right, tree2.left)