from queue import Queue

class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = self.right = None

    def insert_left(self, value):
        if self.left == None:
            self.left = Tree(value)
        else:
            self.left.insert_left(value)

    def insert_right(self, value):
        if self.right == None:
            self.right = Tree(value)
        else:
            self.right.insert_right(value)

    def bfs(self):
        # queue
        queue = Queue()
        queue.put(self)
        while not queue.empty():
            current = queue.get()
            print(current.value)

            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)

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

tree = Tree(9)
tree.insert_left(4)
tree.insert_right(14)

tree.left.insert_left(2)
tree.left.left.insert_left(1)
tree.left.left.insert_right(3)

tree.right.insert_left(10)
tree.right.insert_right(20)

tree.pre_order()
tree.in_order()
tree.post_order()

tree.bfs()