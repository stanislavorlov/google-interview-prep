# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
        
    return result

def sortedSquares2(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    left, right = 0, n-1
    for i in range(n-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            ans[i] = nums[left]
            left += 1
        else:
            ans[i] = nums[right]
            right -= 1
            
    return ans

nums = [-4,-1,0,3,10]
print(sortedSquares2(nums))

nums = [-7,-3,2,3,11]
print(sortedSquares2(nums))