# https://leetcode.com/problems/open-the-lock/
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1:])

            return ans

        if "0000" in deadends:
            return -1

        start = '0000'
        queue = deque([(start, 0)])
        seen = set(deadends)
        seen.add(start)

        while queue:
            node, level = queue.popleft()
            if node == target:
                return level

            for neighbor in neighbors(node):
                if not neighbor in seen:
                    queue.append((neighbor, level + 1))
                    seen.add(neighbor)

        return -1