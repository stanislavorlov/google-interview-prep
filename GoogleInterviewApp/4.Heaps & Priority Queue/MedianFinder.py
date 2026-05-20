# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq


class MedianFinder:

    def __init__(self):
        self.high = []
        self.low = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return float(-self.low[0] + self.high[0]) / 2

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())

medianFinder.addNum(3)
print(medianFinder.findMedian())