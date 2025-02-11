# https://leetcode.com/problems/reverse-string-ii/

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
# then reverse the first k characters and leave the other as original.

#Example 1:

# s = "abcdefgh", k=3 => "cbadefhg"     fewer than k characters left, reverse all of them
# s = "abcdefghij", k=3 => "cbadefihgj"     less than 2k but greater k, reverse the first k

from shlex import join


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(s), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        
        return "".join(a)
    
solution = Solution()
print(solution.reverseStr("abcdefgh", 3))
print(solution.reverseStr("abcdefghij", 3))