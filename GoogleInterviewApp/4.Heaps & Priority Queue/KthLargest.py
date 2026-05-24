# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if val == mid_element:
                return mid
            if val < mid_element:
                right = mid - 1
            else:
                left = mid + 1

        return left

class KLargestHeap:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, num: int) -> None:
        if len(self.heap) < self.k or self.heap[0] < num:
            heapq.heappush(self.heap, num)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        return self.heap[0]

kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)   # return 4
kthLargest.add(5)   # return 5
kthLargest.add(10)  # return 5
kthLargest.add(9)   # return 8
kthLargest.add(4)   # return 8