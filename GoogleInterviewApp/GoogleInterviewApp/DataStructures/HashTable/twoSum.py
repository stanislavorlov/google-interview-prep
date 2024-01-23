from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        map = {}
        for idx, num in enumerate(nums):
            if num in map.keys():
                return [map[num], idx]
            
            dif = target - num
            if dif not in map.keys():
                map[dif] = idx

        return []
    
# nums = [2,7,11,15]
# target = 9
    
# nums = [3,2,4]
# target = 6
    
nums = [3,3]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))