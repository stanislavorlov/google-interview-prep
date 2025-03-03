# Example 3: Given the head of a linked list and an integer k, return the kth node from the end.

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def findNthFromEnd(head: ListNode, k):
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(findNthFromEnd(list, 2).val)