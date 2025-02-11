from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeByIndex(head: ListNode, n):
    dummyHead = ListNode(0, head)
    pre = dummyHead
    cur = head
    for _ in range(n):
        cur = cur.next
        pre = pre.next
    pre.next = cur.next

    return dummyHead.next

def print_list(head: ListNode):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list = removeByIndex(list, 4)
print_list(list)