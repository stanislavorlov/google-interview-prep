# https://leetcode.com/problems/max-area-of-island/description/?source=submission-noac

import unittest

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_area = 0
    visited = set()

    def dfs(row_idx, col_idx):
        visited.add((row_idx, col_idx))

        area = 1

        for dirX, dirY in [(-1,0), (1,0), (0, -1), (0, 1)]:
            new_row, new_col = row_idx + dirX, col_idx + dirY

            if 0 <= new_row < rows and 0 <= new_col < cols \
                    and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                area += dfs(new_row, new_col)

        return area

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                current_area = dfs(row, col)
                max_area = max(max_area, current_area)

    return max_area

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

        self.assertEqual(maxAreaOfIsland(grid), 6)

    def test_case_2(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(maxAreaOfIsland(grid), 0)

    def test_case_3(self):
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]
        ]

        self.assertEqual(maxAreaOfIsland(grid), 4)