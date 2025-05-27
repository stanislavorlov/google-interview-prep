# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/
from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        basket = 5000
        weight.sort()
        max_count = 0

        for w in weight:
            basket -= w
            if basket < 0:
                break
            max_count += 1

        return max_count

    def maxNumberOfApples2(self, weight: List[int]) -> int:
        size = len(weight)+1
        counts = [0] * size
        for w in weight:
            counts[w] += 1

        apples = units = 0
        for i in range(size):
            if counts[i] > 0:
                take = min(counts[i], (5000 - units) // i)
                if take == 0:
                    break

                apples += take
                units += take * i

        return apples

solution = Solution()
print(solution.maxNumberOfApples([100,200,150,1000]))

print(solution.maxNumberOfApples([900,950,800,1000,700,800]))