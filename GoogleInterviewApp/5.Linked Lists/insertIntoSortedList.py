class ListNode:
     def __init__(self, val=0, next=None):
         self._val = val
         self._next = next

def insertIntoSortedList(head: ListNode, val: int):
    newHead = ListNode(0, head)
    prev = newHead

    while head and head._val < val:
        prev = head
        head = head._next

    prev._next = ListNode(val, head)

    return newHead._next

def print_list(head: ListNode):
    pointer = head
    while pointer:
        print(pointer._val)
        pointer = pointer._next

list = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
list = insertIntoSortedList(list, 1)
print_list(list)