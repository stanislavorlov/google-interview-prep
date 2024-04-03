# Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
# and each integer appears once or twice, return an array of all the integers that appears twice.

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        seen = set()
        for n in nums:
            if n in seen:
                ans.append(n)
            else:
                seen.add(n)

        return ans
    
solution = Solution()
print(solution.findDuplicates([1]))