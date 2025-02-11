# https://leetcode.com/problems/sort-array-by-parity-ii/

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]

# Input: nums = [2,3]
# Output: [2,3]

# even % 2 == 0, odd % 2 == 1

# nums.length is even

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenIdx, oddIdx = 0, 1
        res = [-1] * len(nums)

        for n in nums:
            if n % 2 == 0:
                res[evenIdx] = n
                evenIdx += 2
            else:
                res[oddIdx] = n
                oddIdx += 2

        return res
    
    def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
        evenPointer, oddPointer, n = 0, 1, len(nums)
        while evenPointer < n and oddPointer < n:
            if nums[evenPointer] % 2:
                while nums[oddPointer] % 2:
                    oddPointer += 2
                nums[evenPointer], nums[oddPointer] = nums[oddPointer], nums[evenPointer]
            evenPointer += 2
                
        return nums
    
    def sortArrayByParityII3(self, nums: List[int]) -> List[int]:
        evenPointer, oddPointer, n = 0, 1, len(nums)
        while evenPointer < n and oddPointer < n:
            if not nums[evenPointer] % 2:
                evenPointer += 2
            elif nums[oddPointer] % 2:
                oddPointer += 2
            else:
                nums[evenPointer], nums[oddPointer] = nums[oddPointer], nums[evenPointer]
                
        return nums
    
solution = Solution()
print(solution.sortArrayByParityII3([4,2,5,7]))      # -> [4,5,2,7]
print(solution.sortArrayByParityII3([5,7,4,2]))      # -> [4,7,5,2]

print(solution.sortArrayByParityII3([2,3]))          # -> [2,3]

print(solution.sortArrayByParityII3([2,4,6,5,7,9]))  # -> [2,5,4,7,6,9]

print(solution.sortArrayByParityII3([3,4]))          # -> [4, 3]