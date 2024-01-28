# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k.

# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    map = {}
    for i,n in enumerate(nums):
        if n in map and abs(i - map[n]) <= k:
            return True
        map[n] = i
            
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))     #true

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))     #true

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))     #false