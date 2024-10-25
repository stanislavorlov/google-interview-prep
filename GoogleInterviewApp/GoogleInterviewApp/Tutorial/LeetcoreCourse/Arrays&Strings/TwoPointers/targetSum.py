# Given a SORTED array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target

def targetSum(nums: [], target):
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
            
    return False

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(targetSum(nums, target))