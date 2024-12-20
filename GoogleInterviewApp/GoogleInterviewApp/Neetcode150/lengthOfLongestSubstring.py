# https://neetcode.io/problems/longest-substring-without-duplicates
# Given a string s, find the length of the longest substring without duplicate characters.

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        s_map = defaultdict()
        ans = 0

        for idx, right in enumerate(s):
            if right not in s_map:
                s_map[right] = idx
                ans = max(ans, idx - left + 1)
            else:
                while right in s_map:
                    if s[left] in s_map:
                        del s_map[s[left]]
                    left += 1
                s_map[s[idx]] = idx

        return ans

solution = Solution()
print(solution.lengthOfLongestSubstring("zxyzxyz"))     #3

print(solution.lengthOfLongestSubstring("xxxx"))        #1

print(solution.lengthOfLongestSubstring("bbbbb"))        #1