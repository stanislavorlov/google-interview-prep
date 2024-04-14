class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.data:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def print_inorder(self):
        if self.left != None:
            self.left.print_inorder()
        print(self.data)
        if self.right != None:
            self.right.print_inorder()

    def print_preorder(self):
        print(self.data)
        if self.left != None:
            self.left.print_inorder()
        if self.right != None:
            self.right.print_inorder()

    def print_postorder(self):
        if self.left != None:
            self.left.print_inorder()
        if self.right != None:
            self.right.print_inorder()
        print(self.data)

tree = TreeNode(5)
tree.insert(3)
tree.insert(7)
tree.insert(4)
tree.insert(6)
tree.print_postorder()