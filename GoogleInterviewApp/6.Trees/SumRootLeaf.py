# You are given the root of a binary tree containing digits from 0 to 9 only.
# Return the total sum of all root-to-leaf numbers.

# [1,2,3]
# 1->2 + 1->3 = 12 + 13 = 25

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumLeaves(root, 0)

    def sumLeaves(self, node: Optional[TreeNode], sum = 0) -> int:
        if node:
            sum = sum * 10 + node.val
        else:
            return 0
        
        if node.left == None and node.right == None:
            return sum
        
        return self.sumLeaves(node.left, sum) + self.sumLeaves(node.right, sum)
        
    
tree = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.sumNumbers(tree))