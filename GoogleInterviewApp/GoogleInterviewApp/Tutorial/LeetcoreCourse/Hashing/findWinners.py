# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/

# You are given an integer array matches where matches[i] = [winneri, loseri] 
# indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]

# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]

from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losts = defaultdict(int)
        for winner, loser in matches:
            losts[winner] += 0
            losts[loser] += 1
                
        zero_lose, one_lose = [], []
        for k,v in losts.items():
            if v == 0:
                zero_lose.append(k)
            elif v == 1:
                one_lose.append(k)
                
        return [sorted(zero_lose), sorted(one_lose)]
    
solution = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(solution.findWinners(matches))        # [[1,2,10],[4,5,7,8]]

matches = [[2,3],[1,3],[5,4],[6,4]]
print(solution.findWinners(matches))        # [[1,2,5,6],[]]