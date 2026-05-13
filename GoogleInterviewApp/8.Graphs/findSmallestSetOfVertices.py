# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> int:
        matrix = defaultdict(list)

        for a, b in edges:
            matrix[b].append(a)

        output = []
        for i in range(n):
            if i not in matrix:
                output.append(i)

        return output

    def findSmallestSetOfVertices2(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for a, b in edges:
            indegree[b] += 1

        return [node for node in range(n) if indegree[node]==0]