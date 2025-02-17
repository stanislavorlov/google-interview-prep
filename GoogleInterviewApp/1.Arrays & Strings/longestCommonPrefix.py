# https://leetcode.com/problems/longest-common-prefix/
from typing import List


# Write a function to find the longest common prefix string amongst an array of strings.

#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Input: strs = ["dog","racecar","car"]
#Output: ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        while len(strs[0]) > len(output):
            output += strs[0][len(output)]
            if not all(s.startswith(output) for s in strs):
                output = output[:-1]
                break
        return output

solution = Solution()
print(solution.longestCommonPrefix([""]))

print(solution.longestCommonPrefix(["flower","flow","flight"]))

print(solution.longestCommonPrefix(["dog","racecar","car"]))