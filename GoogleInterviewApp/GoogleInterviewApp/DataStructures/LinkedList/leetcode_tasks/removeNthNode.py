from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first != None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next

        return dummy.next
    
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return dummy.next

    def print(self, head: Optional[ListNode]):
        while head != None:
            print(head.val)
            head = head.next

solution = Solution()
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list = solution.removeNthFromEnd2(list, 4)
solution.print(list)