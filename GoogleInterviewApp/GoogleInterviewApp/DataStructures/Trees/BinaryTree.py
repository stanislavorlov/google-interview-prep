class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.data = val

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
            
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

tree = Node(10)
tree.left = Node(5)
tree.right = Node(15)
tree.insert(8)
tree.insert(12)
# print(tree.contains(10))
# print(tree.contains(15))
# print(tree.contains(12))
# print(tree.contains(7))
# print(tree.contains(3))

tree.print_postorder()