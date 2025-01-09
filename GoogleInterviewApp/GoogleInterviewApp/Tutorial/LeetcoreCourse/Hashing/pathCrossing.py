# https://leetcode.com/problems/path-crossing/description/

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
# each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

import unittest

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moving = { 'N': (0,1), 'S': (0,-1), 'E': (1,0), 'W': (-1,0) }
        
        x,y = 0,0
        visited = {(0,0)}
        for p in path:
            dx, dy = moving[p]
            x, y = x + dx, y + dy
            if (x,y) in visited:
                return True
            
            visited.add((x,y))
        
        return False
    
class TestMethods(unittest.TestCase):
    
    def test_case_one(self):
        sol = Solution()
        result = sol.isPathCrossing("NES")
        self.assertEqual(result, False)
        
    def test_case_two(self):
        sol = Solution()
        result = sol.isPathCrossing("NESWW")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()