# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
from idlelib.tree import TreeNode


# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
# The lowest common ancestor of two nodes p and q in a tree T is the lowest node 
# that has both p and q as descendants (where we allow a node to be a descendant of itself)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None

class Solution:
    def lowestCommonAncestor2(self, p: Node, q: Node) -> Node:
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

    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
        stack = [root]

        parent = {root: None}

        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        seen = set()
        while p:
            seen.add(p)
            p = parent[p]

        while not q in seen:
            q = parent[q]
        return q

solution = Solution()
node1 = Node(5, Node(6), Node(2, Node(7), Node(4)))
node2 = Node(1, Node(0), Node(8))
tree = Node(3, node1, node2)
print(solution.lowestCommonAncestor(tree, node1, node2).val)