# https://neetcode.io/problems/is-anagram

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = defaultdict(int), defaultdict(int)
        for s_ch in s:
            s_map[s_ch] += 1
        for t_ch in t:
            t_map[t_ch] += 1

        return s_map == t_map