# https://neetcode.io/problems/anagram-groups

import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for val in strs:
            res[tuple(sorted(val))].append(val)

        return list(res.values())