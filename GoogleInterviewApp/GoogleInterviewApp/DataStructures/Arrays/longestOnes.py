# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def longestOnes2(nums: list[int], k: int) -> int:
    left = 0
    for right in range(len(nums)):
        k -= 1 - nums[right]
        
        if k < 0:
            k += 1 - nums[left]
            left += 1
            
    return right - left + 1

def longestOnes(nums: list[int], k: int) -> int:
    l = ans = 0
    for r, val in enumerate(nums):
        k -= 1 - val
        if k < 0:
            k += 1 - nums[l]
            l += 1
        else:
            ans = max(ans, r-l+1)
    return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print (longestOnes(nums, k))    #6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print (longestOnes(nums, k))    #10

nums = [0,0,0,1]
k = 4

print (longestOnes(nums, k))    #4

nums = [1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0]
print(longestOnes(nums, 2))     #8