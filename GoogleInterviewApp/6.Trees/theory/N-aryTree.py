class TreeNode:
    def __init__(self, data):
        self.data = data
        self.firstChild = None
        self.nextSibling = None

#          1
#       2   3   4
#

root = TreeNode(1)
root.firstChild = TreeNode(2)
root.firstChild.nextSibling = TreeNode(3)
root.firstChild.nextSibling.nextSibling = TreeNode(4)