from typing import Optional

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
        
def isEven(head: Optional[ListNode]):       # even: length % 2 == 0
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        
    return not fast

head = ListNode(1, ListNode(2))
print(isEven(head))