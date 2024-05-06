# https://leetcode.com/problems/path-sum-ii/

# Given the root of a binary tree and an integer targetSum, 
# return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
# Each path should be returned as a list of the node values, not node references.

from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumDfs(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(root: TreeNode, path: list, cur: int):
            nonlocal paths
            if not root:
                return
            cur += root.val
            path.append(root.val)
            if cur == targetSum and not root.left and not root.right:
                paths.append(list(path))
            else:
                dfs(root.left, path, cur)
                dfs(root.right, path, cur)
            path.pop()

        paths = []
        dfs(root, paths, 0)
        return paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        stack = []
        output = []
        stack.append((root, root.val, [root.val]))
        while len(stack):
            (node, sum, path) = stack.pop()

            if node.left:
                leftCopy = path.copy()
                leftCopy.append(node.left.val)
                stack.append((node.left, sum + node.left.val, leftCopy))

            if node.right:
                rightCopy = path.copy()
                rightCopy.append(node.right.val)
                stack.append((node.right, sum + node.right.val, rightCopy))

            if not node.left and not node.right:
                if sum == targetSum:
                    output.append(path)

        return output

solution = Solution()
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

print(solution.pathSum(root, 22))