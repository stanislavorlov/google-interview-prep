# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# 
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:
# 
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:
# 
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        ans, cnt = 0, 0
        n = len(s)
        
        if k > n:
            return ans

        for i in range(k):
            if s[i] in vowel:
                cnt += 1
                
        ans = cnt
        for i in range(k, n):
            if s[i] in vowel:
                cnt += 1
                
            if s[i-k] in vowel:
                cnt -= 1
                
            ans = max(ans, cnt)

        return ans
    
solution = Solution()
print(solution.maxVowels("abciiidef", 3))
print(solution.maxVowels("aeiou", 2))
print(solution.maxVowels("leetcode", 3))