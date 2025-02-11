# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        chars = set()
        for right in range(len(s)):
            if not s[right] in chars:
                chars.add(s[right])
                ans = max(ans, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])
                
        return ans
    
solution = Solution()
print(solution.lengthOfLongestSubstring("abccbabb"))
print(solution.lengthOfLongestSubstring("abcabcbb"))

print(solution.lengthOfLongestSubstring("bbbbb"))