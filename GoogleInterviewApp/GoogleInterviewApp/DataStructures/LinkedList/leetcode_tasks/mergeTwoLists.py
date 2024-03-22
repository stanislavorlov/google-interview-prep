# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)

        pre = head
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        pre.next = list1 if list1 != None else list2

        return head.next
    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        pre = result
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        pre.next = list1 if list1 != None else list2
        return result.next

    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        head = result
        while list1 and list2:
            if list2.val <= list1.val:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next
            result = result.next

        result.next = list1 if list1 else list2
        return head.next

    def print(self, list: ListNode | None):
        pointer = list
        while pointer:
            print(pointer.val)
            pointer = pointer.next

solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
# [1,1,2,3,4,4]
result = solution.mergeTwoLists3(list1, list2)
solution.print(result)