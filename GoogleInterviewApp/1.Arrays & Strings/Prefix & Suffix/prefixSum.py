# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, 
# return a boolean array that represents the answer to each query. 
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

# For example, given 
#   nums = [1, 6, 3, 2, 7, 2]
#   queries = [[0, 3], [2, 5], [2, 4]]
#   limit = 13
#   answer is [true, false, true]. 
#   For each query, the subarray sums are [12, 14, 12].

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
        
    ans = []
    for x,y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)
        
    return ans

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

print(answer_queries(nums, queries, limit))

# Example 2: 2270. Number of Ways to Split Array
# Given an integer array nums, find the number of ways to split the array into two parts 
# so that the first section has a sum greater than or equal to the sum of the second section. 
# The second section should have at least one number.

def waysToSplitArray(nums: list[int]) -> int:
    n = len(nums)
    
    prefix = [nums[0]]
    for i in range(n):
        prefix.append(nums[i] + prefix[-1])
        
    ans = 0
    for i in range(n - 1):
        left = prefix[i]
        right = prefix[-1] - prefix[i]
        if left >= right:
            ans += 1
            
    return ans