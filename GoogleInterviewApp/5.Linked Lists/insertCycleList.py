# insert a value into sorted cyclic list
# after insertion list should remain as cyclic
# 3 -> 4 -> 1 -> 3      ->      3 -> 4 -> 1 -> 2 -> 3 

from typing import Optional

from DataStructures.LinkedList.Summary import ListNode

class Solution:
    def insert(self, head: Optional[ListNode], insertVal: int) -> ListNode:
        return ListNode(0)