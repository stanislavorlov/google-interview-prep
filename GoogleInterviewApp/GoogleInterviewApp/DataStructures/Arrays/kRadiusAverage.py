# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i with the radius k is 
# the average of all elements in nums between the indices i - k and i + k (inclusive). 
# If there are less than k elements before or after the index i, then the k-radius average is -1.

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        averages = [-1] * n

        window_size = 2*k + 1
        window_sum = sum(nums[:window_size])
        
        averages[k] = window_sum // window_size
        
        for i in range(window_size, n):
            window_sum = window_sum - nums[i - window_size] + nums[i]
            averages[i-k] = window_sum // window_size
            
        return averages
    
    def getAverages2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2*k + 1
        averages = [-1] * n
        window_sum = sum(nums[:window_size])
        
        if window_size > n:
            return nums
        
        averages[k] = window_sum // window_size

        for i in range(window_size, n):
            averages[i-k] = (window_sum + nums[i] - nums[i - window_size]) // window_size
            
        return averages

nums = [7,4,3,9,1,8,5,2,6]
k = 3
# [-1,-1,-1,5,4,4,-1,-1,-1]
# avg[0]=avg[1]=avg[2] = -1
# avg[3] = (nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+nums[5]+nums[6]) / 7
# avg[4] = (nums[1]+nums[2]+nums[3]+nums[4]+nums[5]+nums[6]+nums[7]) / 7

solution = Solution()
print(solution.getAverages(nums, k))

print(solution.getAverages2(nums, k))