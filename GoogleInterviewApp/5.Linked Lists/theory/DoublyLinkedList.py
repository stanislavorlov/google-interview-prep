from typing import Optional

class DoublyNode:
    def __init__(self, value) -> None:
        self.prev = None
        self.next = None
        self.val = value

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = DoublyNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def addHead(self, value):
        new_node = DoublyNode(value)
        head = self.head
        new_node.next = head
        head.prev = new_node
        head = new_node

    def addTail(self, value):
        new_node = DoublyNode(value)
        tail = self.tail
        new_node.prev = tail
        tail.next = new_node
        tail = new_node

    def removeHead(self):
        if self.head == self.tail:      #only if 1 element left or both None
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeTail(self):
        prev = self.tail.prev
        self.tail.prev = None
        prev.next = None
        self.tail = prev

    def removeNode(self, value):
        dummyHead = DoublyNode(0)
        dummyHead.next = self.head
        self.head.prev = dummyHead
        pre = dummyHead
        cur = self.head

        while cur:
            if cur.val == value:
                pre.next = cur.next
            cur = cur.next

        self.head = dummyHead


    def find(self, value) -> Optional[DoublyNode]:
        
        return None

    def get(self, index: int) -> Optional[DoublyNode]:

        return None