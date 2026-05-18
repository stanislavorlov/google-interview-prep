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

    def openLock2(self, deadends: List[str], target: str) -> int:
        next_slot = {
            '0': '1',
            '1': '2',
            '2': '3',
            '3': '4',
            '4': '5',
            '5': '6',
            '6': '7',
            '7': '8',
            '8': '9',
            '9': '0'
        }
        prev_slot = {
            '0' : '9',
            '1' : '0',
            '2' : '1',
            '3' : '2',
            '4' : '3',
            '5' : '4',
            '6' : '5',
            '7' : '6',
            '8' : '7',
            '9' : '8',
        }

        visited = set(deadends)
        pending = deque()
        turns = 0

        if "0000" in visited:
            return -1

        pending.append("0000")
        visited.add("0000")

        while pending:
            curr_level_count = len(pending)
            for _ in range(curr_level_count):
                node = pending.popleft()

                if node == target:
                    return turns

                for wheel in range(4):
                    new_combination = list(node)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = ''.join(new_combination)

                    if new_combination_str not in visited:
                        pending.append(new_combination_str)
                        visited.add(new_combination_str)

                    new_combination = list(node)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = ''.join(new_combination)

                    if new_combination_str not in visited:
                        pending.append(new_combination_str)
                        visited.add(new_combination_str)

            turns += 1

        return -1