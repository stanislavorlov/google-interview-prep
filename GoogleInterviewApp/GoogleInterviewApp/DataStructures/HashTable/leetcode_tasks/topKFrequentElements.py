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
    
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2

print(solution.topKFrequent(nums, k))
print(solution.topKFrequent2(nums, k))