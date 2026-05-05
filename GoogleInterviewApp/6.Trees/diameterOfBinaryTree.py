#  https://leetcode.com/problems/diameter-of-binary-tree/editorial/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameter(self, root: TreeNode) -> int:
        diameter = 0

        def dfs(node):
            if not node:
                return -1

            nonlocal diameter

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            diameter = max(diameter, left_path + right_path + 2)

            return max(left_path, right_path) + 1

        dfs(root)
        return diameter

solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

print(solution.diameter(root))