# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def isValid(row: int, col: int) -> bool:
            return 0 <= row < n and 0 <= col < n

        queue = deque([(0,0,1)])
        visited = set()
        n = len(grid)

        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

        while queue:
            row, col, path = queue.popleft()

            if (row, col) == (n-1, n-1):
                return path

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if isValid(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path + 1))

        return -1