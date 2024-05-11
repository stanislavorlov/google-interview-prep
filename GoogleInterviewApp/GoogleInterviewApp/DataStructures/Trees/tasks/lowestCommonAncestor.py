# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
# The lowest common ancestor of two nodes p and q in a tree T is the lowest node 
# that has both p and q as descendants (where we allow a node to be a descendant of itself)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        hash_Set = set()
        while p and q:
            if p == q:
                return p
            if p in hash_Set:
                return p
            if q in hash_Set:
                return q
            if p.parent:
                hash_Set.add(p)
                p = p.parent
            if q.parent:
                hash_Set.add(q)
                q = q.parent

        return None