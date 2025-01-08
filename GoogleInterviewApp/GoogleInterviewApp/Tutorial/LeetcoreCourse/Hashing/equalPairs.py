# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import defaultdict
from typing import List
import unittest

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        matrix_map = defaultdict(int)
        
        # traverse over the rows
        for row in grid:
            matrix_map[tuple(row)] += 1
            
        counter = 0
        # travers overs the cols
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            counter += matrix_map[tuple(col)]
            
        return counter

class TestMethods(unittest.TestCase):
    
    def test_case_one(self):
        solution = Solution()
        grid = [[3,2,1],[1,7,6],[2,7,7]]
        result = solution.equalPairs(grid)
        self.assertEqual(result, 1)

    def test_case_two(self):
        solution = Solution()
        grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
        result = solution.equalPairs(grid)
        self.assertEqual(result, 3)
        
    def test_case_three(self):
        solution = Solution()
        grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
        result = solution.equalPairs(grid)
        self.assertEqual(result, 3)
        
        # [3,1,2,2]
        # [1,4,4,4]
        # [2,4,2,2]
        # [2,5,2,2]

    def test_case_four(self):
        solution = Solution()
        grid = [[13,13],[13,13]]
        result = solution.equalPairs(grid)
        self.assertEqual(result, 4)
        
        # [13,13]
        # [13,13]

if __name__ == '__main__':
    unittest.main()