# A heap is one of many ways to implement a priority queue

# Add an element in O(log n)
# Remove the minimum element in O(log n)
# Find the minimum element in O(1)

# binary heap can be implemented using an array
# others via tree or graph

# [0] - root elements
# [1], [2] - children of root
# [3], [4] - children of [1]
# [5], [6] - children of [2]
#
# children of [i]: 2*i+1, 2*i+2
#
# parent.val <= child.val

# A heap is a great option whenever you need to find the maximum or minimum of something repeatedly.

from heapq import *
import heapq

heap = []

heappush(heap, 2)
heappush(heap, 1)
heappush(heap, 3)

print(f"minimum elem: {heap[0]}")       # 1

# pop minimum element
heappop(heap)

print('convert a list to heap into linear time')
nums = [43, 2, 13, 634, 120]
heapify(nums)
print(nums)

print('before heap')
heap = [67, 341, 234, -67, 12, -976]
print(heap)

heapq.heapify(heap)
heapq.heappush(heap, 7451)
heapq.heappush(heap, -5352)

print('numbers in sorted order')
while heap:
    print(heapq.heappop(heap))