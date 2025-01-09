# https://leetcode.com/problems/destination-city/

# You are given the array paths, where paths[i] = [cityAi, cityBi] means 
# there exists a direct path going from cityAi to cityBi. Return the destination city, 
# that is, the city without any path outgoing to another city.

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"

# Input: paths = [["A","Z"]]
# Output: "Z"

from collections import defaultdict
from typing import List
import unittest

class Solution:
    def destCity2(self, paths: List[List[str]]) -> str:
        dest = defaultdict(list)
        
        for path in paths:
            dest[path[0]].append(path[1])
            dest[path[1]] = dest[path[1]] if path[1] in dest else []
            
        return next((key for key, val in dest.items() if len(val) == 0), None)
    
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_set = set()
        for path in paths:
            outgoing_set.add(path[0])
            
        for path in paths:
            if path[1] not in outgoing_set:
                return path[1]
            
        return ""

class TestMethods(unittest.TestCase):
    
    def test_first(self):
        solution = Solution()
        ans = solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
        
        self.assertEqual(ans, "Sao Paulo")
        
    def test_second(self):
        solution = Solution()
        ans = solution.destCity([["B","C"],["D","B"],["C","A"]])
        
        self.assertEqual(ans, "A")
        
    def test_third(self):
        solution = Solution()
        ans = solution.destCity([["A","Z"]])
        
        self.assertEqual(ans, "Z")
        
if __name__ == '__main__':
    unittest.main()