def check_for_target(nums, target):
    left, right = 0, len(nums) - 1
    iter = 0
    while left < right:
        sum = nums[left] + nums[right]
        iter += 1
        if sum == target:
            print(iter)
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
            
    print(iter)
    return False

nums = [1,2,4,6,8,9,14,15]
print(check_for_target(nums, 13))