# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional


# maximum sum of twins nodes
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
# These are the only nodes with twins for n = 4

# Input: head = [5,4,2,1]
# Output: 6

# Input: head = [4,2,2,3]
# Output: 7

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# find the middle
# reverse the second half of the list
# create another fast pointer n/2 ahead of slow

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        tail = prev
        prev = None

        while slow:
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_

        tail.next = prev
        ans = 0
        while head and prev:
            ans = max(ans, head.val+prev.val)
            head = head.next
            prev = prev.next

        return ans

sol = Solution()
head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print(sol.pairSum(head))

head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
print(sol.pairSum(head))