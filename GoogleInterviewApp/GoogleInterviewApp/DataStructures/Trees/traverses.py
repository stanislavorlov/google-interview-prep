from queue import Queue

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = self.right
            self.right = new_node

def pre_order(root: TreeNode):
    print(root.value)

    if root.left:
        pre_order(root.left)

    if root.right:
        pre_order(root.right)

def in_order(root: TreeNode):
    if root.left:
        in_order(root.left)

    print(root.value)

    if root.right:
        in_order(root.right)

def post_order(root: TreeNode):
    if root.left:
        post_order(root.left)

    if root.right:
        post_order(root.right)

    print(root.value)

# Breadth-First Search
def bfs(root: TreeNode):
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        print(current.value)

        if current.left:
            queue.put(current.left)

        if current.right:
            queue.put(current.right)

def depth_first_iterative(root: TreeNode):
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.value)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

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

tree = TreeNode(9)
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
pre_order(tree)

# 2. in-order
print("in-order")
in_order(tree)

# 3. post-order
print("post-order")
post_order(tree)

# 4. Breadth-First search                   

# levels
# level 0
# level 1
# level 2

print("BFS")
bfs(tree)

print("DFS Interactive")
depth_first_iterative(tree)