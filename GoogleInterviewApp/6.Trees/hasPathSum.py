import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            if not node.left and not node.right:
                return curSum + node.val == targetSum

            left = dfs(node.left, curSum + node.val)
            right = dfs(node.right, curSum + node.val)

            return left or right

        return dfs(root, 0)

    def hasPathSumIteractive(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        while stack:
            node, curSum = stack.pop()
            if not node.left and not node.right:
                if curSum + node.val == targetSum:
                    return True

            if node.left:
                stack.append((node.left, curSum + node.val))
            if node.right:
                stack.append((node.right, curSum + node.val))

        return False

    def hasPathSumOptimal(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        de = [
            (root, targetSum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

class TestHasPathSum(unittest.TestCase):
    def test1(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
        actual = Solution().hasPathSumIteractive(root, 22)

        self.assertEqual(actual, True)

    def test2(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        actual = Solution().hasPathSumIteractive(root, 5)

        self.assertEqual(actual, False)

    def test3(self):
        self.assertEqual(Solution().hasPathSumIteractive(None, 0), False)