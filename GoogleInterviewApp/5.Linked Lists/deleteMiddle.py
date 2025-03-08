# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next

        return dummy.next

    def print_list(self, head: Optional[ListNode]):
        pointer = head
        while pointer:
            print(pointer.val)
            pointer = pointer.next

solution = Solution()
head = ListNode(1,ListNode(3, ListNode(4, ListNode(7,ListNode(1, ListNode(2,ListNode(6)))))))

head = solution.deleteMiddle(head)
print('list 1')
solution.print_list(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

head = solution.deleteMiddle(head)
print('list 2')
solution.print_list(head)

head = ListNode(2, ListNode(1))

head = solution.deleteMiddle(head)
print('list 3')
solution.print_list(head)

head = ListNode(1)

head = solution.deleteMiddle(head)
print('list 4')
solution.print_list(head)