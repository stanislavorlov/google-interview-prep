# https://leetcode.com/problems/same-tree/description/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # iteration
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deq = deque([(p,q),])
        while deq:
            p, q = deq.popleft()
            if not self.checkNode(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
            
    def checkNode(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2:
            return True
        
        if not n1 or not n2:
            return False
        
        return n1.val == n2.val
