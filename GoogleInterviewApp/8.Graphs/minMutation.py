# https://leetcode.com/problems/minimum-genetic-mutation/description/
import unittest
from collections import deque, defaultdict
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visited = set(startGene)
        while queue:
            gene, level = queue.popleft()
            if gene == endGene:
                return level

            for ch in "ACGT":
                for i in range(len(gene)):
                    neighbor = gene[:i] + ch + gene[i + 1:]
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

        return -1

class Test(unittest.TestCase):
    def test1(self):
        startGene = 'AACCGGTT'
        endGene = 'AACCGGTA'
        bank = ["AACCGGTA"]
        solution = Solution()
        self.assertEqual(1, solution.minMutation(startGene, endGene, bank))

    def test2(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        solution = Solution()
        self.assertEqual(2, solution.minMutation(startGene, endGene, bank))