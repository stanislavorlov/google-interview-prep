# find the longest subarray with a sum less than or equal K
# find the longest substring that has more than one "0"
# find the number of subarrays that have a product less than K

# longest subarray
def find_length_subarr(nums, k):
    left = cur = ans = 0
    for right in range(len(nums)):
        cur += nums[right]
        while cur > k:
            cur -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
        
    return ans

def find_longest_subarr(nums, k):
    left = cur = 0
    ans = []
    for right in range(len(nums)):
        cur += nums[right]
        while cur > k:
            cur -= nums[left]
            left += 1
        if right - left + 1 > len(ans):
            ans = nums[left:right+1]
        
    return ans
        
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

print(find_longest_subarr(nums, k))

# longest substring that has more than one "0"
def find_length_substr(s):
    left = cur = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            cur += 1
        while cur > 1:
            if s[left] == "0":
                cur -= 1
            left += 1
        ans = max(ans, right - left + 1)
        
    return ans

s = "1101100111"
print(find_length_substr(s))