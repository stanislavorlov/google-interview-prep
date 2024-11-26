# https://neetcode.io/problems/top-k-elements-in-list

import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.defaultdict(int)
        for n in nums:
            frequency[n] += 1
            
        freq_val = collections.defaultdict(list)
        for key,val in frequency.items():
            freq_val[val].append(key)
            
        freq_keys = sorted(freq_val.keys(), reverse= True)
        output = []
        idx = 0
        while k > 0:
            try:
                output.append(freq_val[freq_keys[idx]].pop())
                k -= 1
            except:
                idx += 1

        return output