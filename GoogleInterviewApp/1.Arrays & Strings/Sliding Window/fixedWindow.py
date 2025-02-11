# Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

def find_best_subarray(nums, k):
    sum = 0
    for i in range(k):
        sum += nums[i]
        
    ans = sum
    for i in range(k, len(nums)):
        sum += nums[i] - nums[i-k]
        ans = max(ans, sum)
        
    return ans

k = 4
arr = [3,-1,4,12,-8,5,6]

print(find_best_subarray(arr, k))

#18
#7
#11
#13