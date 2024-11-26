# https://leetcode.com/problems/heaters/
# 
# Every house can be warmed, as long as the house is within the heater's warm radius range. 
#
# Given the positions of houses and heaters on a horizontal line, 
# return the minimum radius standard of heaters so that those heaters could cover all houses.

# houses = [1,2,3], heaters = [2]
# output: 1
# heater at position 2, radius 1 standard

# houses = [1,2,3,4], heaters = [1,4]
# output: 1
# heaters were placed at positions 1,4. We need to use radius 1 standard

# houses = [1,5], heaters = [2]
# output = 3

import sys
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
