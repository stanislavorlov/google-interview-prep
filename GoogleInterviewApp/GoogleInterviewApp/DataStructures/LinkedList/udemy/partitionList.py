# https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5836830#overview

# Implement the partition_list member function for the LinkedList class, 
# # which partitions the list such that all nodes with values less than x 
# come before nodes with values greater than or equal to x.

# Input:
# 
# Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1, x: 5

# Output

# Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        beforeHead = Node(0)
        afterHead = Node(0)
        beforePointer = beforeHead
        afterPointer = afterHead

        pointer = self.head
        prev = None
        while pointer:
            if pointer.value < x:
                beforePointer.next = pointer
                beforePointer = beforePointer.next
            else:
                afterPointer.next = pointer
                afterPointer = afterPointer.next

            prev = pointer
            pointer = pointer.next
            prev.next = None

        beforePointer.next = afterHead.next

        return beforeHead.next
    
list = LinkedList(3)
list.append(1)
list.append(4)
list.append(2)
list.append(5)

result = list.partition_list(3)

cur = result
while cur:
    print(cur.value)
    cur = cur.next