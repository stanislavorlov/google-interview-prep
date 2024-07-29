from queue import Empty

class LinkedQueue:

    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        node = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return node._element

    def enqueue(self, e):
        node = self.Node(e, None)
        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

lq = LinkedQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(3)

print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())