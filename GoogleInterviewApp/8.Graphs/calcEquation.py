import unittest
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(start, end):
            if not start in graph:
                return -1

            seen = {start}
            stack = [(start, 1)]

            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio

                for edge in graph[node]:
                    if not edge in seen:
                        seen.add(edge)
                        stack.append((edge, ratio * graph[node][edge]))

            return -1

        graph = defaultdict(dict)
        for idx in range(len(equations)):
            a, b = equations[idx]
            graph[a][b] = values[idx]
            graph[b][a] = 1 / values[idx]

        ans = []
        for query in queries:
            ans.append(dfs(query[0], query[1]))

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

        actual = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(actual, [6.00000,0.50000,-1.00000,1.00000,-1.00000])

    def test2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

        actual = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(actual, [3.75000,0.40000,5.00000,0.20000])

    def test3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]

        actual = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(actual, [0.50000,2.00000,-1.00000,-1.00000])