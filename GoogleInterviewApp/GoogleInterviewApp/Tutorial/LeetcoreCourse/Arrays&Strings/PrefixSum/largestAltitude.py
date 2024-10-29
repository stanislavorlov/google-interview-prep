# https://leetcode.com/problems/find-the-highest-altitude/

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

import sys
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, highest = 0, 0
        
        for n in gain:
            altitude += n
            highest = max(highest, altitude)
            
        return highest
    
solution = Solution()
print("first")
print(solution.largestAltitude([-5,1,5,0,-7]))
print("second")
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))