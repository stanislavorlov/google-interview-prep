# https://neetcode.io/problems/buy-and-sell-crypto

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# 
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        result = 0
        for i in range(1, len(prices)):
            min_val = min(min_val, prices[i])
            result = max(result, prices[i] - min_val)
            
        return result
    
solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))

print(solution.maxProfit([10,8,7,5,2]))