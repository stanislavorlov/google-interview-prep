# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        start_row, start_col = entrance
        queue = deque([(start_row, start_col, 0)])

        # instead of visited, we can modify the . into + once a cell is visited
        visited = {(start_row, start_col)}

        while queue:
            r, c, steps = queue.popleft()

            if (r != start_row or c != start_col) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if not (nr, nc) in visited:
                        queue.append((nr, nc, steps + 1))
                        visited.add((nr, nc))

        return -1

    def nearestExistInPlace(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        start_row, start_col = entrance
        # mark visited square
        maze[start_row][start_col] = '+'

        queue = deque([(start_row, start_col, 0)])

        while queue:
            row, col, steps = queue.popleft()

            for d in dirs:
                next_row, next_col = row + d[0], col + d[1]

                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':
                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:
                        return steps + 1

                    maze[next_row][next_col] = '+'
                    queue.append((next_row, next_col, steps + 1))

        return -1


solution = Solution()
print(solution.nearestExistInPlace([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))    # 1

print(solution.nearestExistInPlace([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))     # 2