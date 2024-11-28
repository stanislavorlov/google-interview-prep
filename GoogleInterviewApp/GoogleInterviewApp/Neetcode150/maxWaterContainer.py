# https://neetcode.io/problems/max-water-container

# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea2(self, heights: List[int]) -> int:
        answer = 0
        for r in range(len(heights)):
            l = 0
            while l <= r:
                square = (r - l) * min(heights[l], heights[r])
                answer = max(answer, square)
                l += 1
        
        return answer
    
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        l, r = 0, len(heights) - 1
        while l < r:
            square = (r - l) * min(heights[l], heights[r])
            answer = max(answer, square)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return answer

solution = Solution()
height = [1,7,2,5,4,7,3,6]
print(solution.maxArea(height))     # 36

height = [2,2,2]
print(solution.maxArea(height))     # 4