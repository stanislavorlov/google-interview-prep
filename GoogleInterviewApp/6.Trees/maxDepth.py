class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth2(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if node:
                stack.append((current_depth + 1, node.left))
                stack.append((current_depth + 1, node.right))
                depth = max(depth, current_depth)

        return depth

tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

tree2 = TreeNode(1, None, TreeNode(2))

print(Solution().maxDepth2(tree1))
print(Solution().maxDepth2(tree2))