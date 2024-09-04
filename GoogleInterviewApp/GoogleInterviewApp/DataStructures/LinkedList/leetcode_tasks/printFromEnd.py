# print linked list from the end
from typing import Optional

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def print_list(head: Optional[ListNode]):
    if not head:
        return
    
    print_list(head.next)
    
    print(head.val)
    
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(list)