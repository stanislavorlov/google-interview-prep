import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.xorPtr = 0

def xor(a, b):
    return a ^ b

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.address_map = {}

    def get_pointer(self, node):
        if node is None:
            return 0
        addr = id(node)
        self.address_map[addr] = node  # Store reference

        return addr

    def dereference_pointer(self, address):
        return self.address_map.get(address, None)

    def insert(self, data):
        new_node = Node(data)
        new_node.xorPtr = self.get_pointer(self.tail)

        if self.tail:
            self.tail.xorPtr ^= self.get_pointer(new_node)
        else:
            self.head = new_node

        self.tail = new_node

    def traverse_forward(self):
        prev_addr = 0
        cur = self.head
        while cur:
            print(cur.data)
            next_addr = prev_addr ^ cur.xorPtr
            prev_addr = self.get_pointer(cur)
            cur = self.dereference_pointer(next_addr)

    def traverse_backward(self):
        prev_addr = 0
        cur = self.tail
        while cur:
            print(cur.data)
            next_addr = prev_addr ^ cur.xorPtr
            prev_addr = self.get_pointer(cur)
            cur = self.dereference_pointer(next_addr)

xor_list = XORLinkedList()
xor_list.insert(1)
xor_list.insert(2)
xor_list.insert(3)
xor_list.insert(4)

xor_list.traverse_forward()

xor_list.traverse_backward()