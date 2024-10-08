# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# timeout limit exceeded
def longestOnes2(nums: list[int], k: int) -> int:
    ans = 0
    for left in range (len(nums)):
        attemp = k
        right = left
        while right < len(nums) and (attemp or nums[right] == 1):
            if nums[right] == 0:
                attemp -= 1
            right += 1
        ans = max(ans, right - left)

    return ans

def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    for right in range(len(nums)):
        k -= 1 - nums[right]
        if k < 0:
            k += 1 - nums[left]
            left += 1
            
    return right - left + 1

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print (longestOnes(nums, k))    #6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print (longestOnes(nums, k))    #10