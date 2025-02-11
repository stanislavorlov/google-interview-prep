# https://leetcode.com/problems/top-k-frequent-elements/editorial/

import collections
from typing import List

class Solution:
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        answer = []
        
        for k,v in counter.most_common(k):
           answer.append(k)
        
        return answer
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return [k for k,v in collections.Counter(nums).most_common(k)]
    
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        map, frequencies, ans = {}, collections.defaultdict(list), []
        for n in nums:
            map[n] = map.get(n, 0) + 1

        for _k, _v in map.items():
            if not _k in frequencies[_v]:
                frequencies[_v].append(_k)

        sorted_list = sorted(frequencies.keys(), reverse=True)
        for key in sorted_list:
            for i in frequencies[key]:
                ans.append(i)
                k-=1
                if k <= 0:
                    return ans

        return ans
    
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
    
solution = Solution()
nums = [1,2,2,3,3,4]
k = 2
print(solution.topKFrequent(nums, k))

nums = [5,5,5,6,6,7]
k = 2

print(solution.topKFrequent(nums, k))
# print(solution.topKFrequent2(nums, k))
# print(solution.topKFrequent3(nums, k))