# https://leetcode.com/problems/number-of-islands/description/

from typing import List


class Solution:
    def numIsland(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    ans += 1
                    seen.add((row, col))
                    dfs(row, col)

        return ans

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            if (
                    r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"  # (r,c) in visited
            ):
                return

            grid[r][c] = "0"
            # visited.add((r,c))

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(r + dx, c + dy)

        num_islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands

    def numIslands3(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r: int, c: int):
            # Fix 1: Stop DFS if the cell is water ("0")
            if (
                    r < 0 or r >= len(grid) or
                    c < 0 or c >= len(grid[0]) or
                    (r, c) in visited or
                    grid[r][c] == "0"
            ):
                return

            visited.add((r, c))

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(r + dx, c + dy)

        num_islands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Fix 2: Check if the land has already been visited
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    num_islands += 1

        return num_islands