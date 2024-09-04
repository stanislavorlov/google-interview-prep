from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin = head
        pre = None
        pointer = head
        while pointer != None:
            post = pointer.next
            pointer.next = pre
            pre = pointer
            pointer = post
        if begin != None:
            begin.next = None

        return pre
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur != None:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
    
    def print(self, head: Optional[ListNode]):
        pointer = head
        while pointer != None:
            print(pointer.val)
            pointer = pointer.next

solution = Solution()
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list = ListNode(1, ListNode(2))
#solution.print(list)
list = solution.reverseList(list)
solution.print(list)