import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
    
solution = Solution()
nums = [5,5,5,6,6,7]
k = 2

print(solution.topKFrequent(nums, k))
print(solution.topKFrequent2(nums, k))
print(solution.topKFrequent3(nums, k))