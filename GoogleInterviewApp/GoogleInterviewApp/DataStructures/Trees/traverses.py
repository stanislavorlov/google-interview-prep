from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def pre_order(self):
        print(self.value)

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.value)

        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(self.value)

    # Breadth-First Search
    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current = queue.get()
            print(current.value)

            if current.left:
                queue.put(current.left)

            if current.right:
                queue.put(current.right)

# in-order
# left
# print
# right

# pre-order
# print
# left
# right

# post-order
# left
# right
# print

# bfs
# queue current
# while
# print
# queue left
# queue right

tree = BinaryTree(9)
tree.insert_left(4)
tree.insert_right(14)

tree.left.insert_left(2)
tree.left.left.insert_left(1)
tree.left.left.insert_right(3)

tree.right.insert_left(10)
tree.right.insert_right(20)

#               9
#         4              14
#     2             10      20     
# 1     3
# Depth-First Search

# 1. pre-order
print("Pre order")
#tree.pre_order()

# 2. in-order
print("in-order")
#tree.in_order()

# 3. post-order
print("post-order")
#tree.post_order()

# 4. Breadth-First search                   

# levels
# level 0
# level 1
# level 2

print("BFS")
tree.bfs()