# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence.

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

import collections


class Solution:
    def groupString(self, strings: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for str in strings:
            key = tuple((ord(c) - ord(str[0])) % 26 for c in str)
            ans[key].append(str)
        return ans.values()
    
solution = Solution()
strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(solution.groupString(strings))
strings = ["az", "ba"]
print(solution.groupString(strings))
#
strings = ["a"]
print(solution.groupString(strings))

#print(26 - abs(ord('a') - ord('z')))    #1
#print(26 - abs(ord('z') - ord('a')))    #1