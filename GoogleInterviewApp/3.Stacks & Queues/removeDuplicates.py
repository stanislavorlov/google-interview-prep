# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
from collections import deque


# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# Input: s = "abbaca"
# Output: "ca"

# Input: s = "azxxzy"
# Output: "ay"

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

solution = Solution()
print(solution.removeDuplicates("abbaca"))

print(solution.removeDuplicates("azxxzy"))