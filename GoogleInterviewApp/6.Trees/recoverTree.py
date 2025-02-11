# https://leetcode.com/problems/recover-binary-search-tree/
# You are given the root of a binary search tree (BST), 
# where the values of exactly two nodes of the tree were swapped by mistake. 
# Recover the tree without changing its structure.

from typing import Optional
from DataStructures.Trees.Tasks import TreeNode

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        