class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        pre = self.head
        cur = self.head
        while cur.next:
            pre = cur
            cur = cur.next
        pre.next = None
        self.tail = pre
        self.length -= 1
        return cur

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.tail = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
                return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.head = self.head.next
        else:
            if index == self.length - 1:
                if self.length < 2:
                    self.head = None
                    self.tail = None
                else:
                    tmp = self.get(self.length - 2)
                    self.tail = tmp
                    tmp.next = None
            else:
                tmp = self.get(index)
                pre = self.get(index - 1)
                pre.next = tmp.next
                
        self.length -= 1

    def reverse(self):
        before = None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.print_list()