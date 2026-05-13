# https://leetcode.com/problems/01-matrix/description/

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m, n = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        seen = set()
        matrix = [row[:] for row in mat]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                if (new_row, new_col) not in seen and is_valid(new_row, new_col):
                    queue.append((new_row, new_col, steps + 1))
                    seen.add((new_row, new_col))

                    matrix[new_row][new_col] = steps + 1

        return matrix