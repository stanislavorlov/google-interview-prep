import unittest
from typing import List


class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        answer = 0
        for cost in costs:
            if coins >= cost:
                answer += 1
                coins -= cost
            else:
                break

        return answer

    def maxIceCream2(self, costs: List[int], coins: int) -> int:
        m = max(costs)

        counter = [0] * (m+1)
        for cost in costs:
            counter[cost] += 1
        answer = 0
        for i in range(1, m+1):
            amount = min(i * counter[i], coins)
            if coins - amount >= 0:
                answer += min(counter[i], coins // i)
                coins -= amount

            if coins <= 0:
                break

        return answer

class TestMaxIceCream(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        costs = [1,3,2,4,1]
        coins = 7

        self.assertEqual(self.solution.maxIceCream2(costs, coins), 4)

    def test_second(self):
        costs = [10, 6, 8, 7, 7, 8]
        coins = 5

        self.assertEqual(self.solution.maxIceCream2(costs, coins), 0)

    def test_third(self):
        costs = [1, 6, 3, 1, 2, 5]
        coins = 20

        self.assertEqual(self.solution.maxIceCream2(costs, coins), 6)

    def test_fourth(self):
        costs = [4,7,6,4,4,2,2,4,8,8]
        coins = 41

        self.assertEqual(self.solution.maxIceCream2(costs, coins), 9)