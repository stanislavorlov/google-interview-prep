from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# [1,2,2,1]     true
# [1,2]         false
# [1,2,3,4,5]
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # fast-slow pointer to find a middle

        # slow is a start of second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse half of the list
        pre, cur = None, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        # 2 pointers to checks if halfs are equal
        first_half, second_half = head, pre
        # head, pre
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
    
solution = Solution()
list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(solution.isPalindrome(list))
list = ListNode(1, ListNode(2, ListNode(3)))
print(solution.isPalindrome(list))