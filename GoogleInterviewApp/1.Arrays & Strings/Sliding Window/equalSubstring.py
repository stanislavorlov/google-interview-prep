# https://leetcode.com/problems/get-equal-substrings-within-budget/

# You are given two strings s and t of the same length and an integer maxCost.
# Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left, right = 0, 0
        ans = 0
        for right in range(n):
            maxCost -= abs(ord(s[right]) - ord(t[right]))
            
            while maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans
    
solution = Solution()
print(solution.equalSubstring("abcd", "bcdf", 3))

print(solution.equalSubstring("abcd", "cdef", 3))

print(solution.equalSubstring("abcd", "acde", 0))