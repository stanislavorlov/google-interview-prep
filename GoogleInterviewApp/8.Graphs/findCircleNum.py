# https://leetcode.com/problems/number-of-provinces/

from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # def dfs(node):
        #     for neighbor in graph[node]:
        #         if neighbor not in seen:
        #             seen.add(neighbor)
        #             dfs(neighbor)

        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        graph = defaultdict(list)
        n = len(isConnected)

        # build graph
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0
        for edge in range(n):
            if edge not in seen:
                dfs(edge)
                ans += 1
                seen.add(edge)

        return ans

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:

        def dfs(node, connected, visit):
            visit[node] = True
            for j in range(len(connected)):
                if isConnected[node][j] and not visited[j]:
                    dfs(j, connected, visit)

        size = len(isConnected)
        numberOfComponents = 0
        visited = [False] * size

        for i in range(size):
            if not visited[i]:
                numberOfComponents += 1
                dfs(i, isConnected, visited)

        return numberOfComponents

solution = Solution()
isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
print(solution.findCircleNum2(isConnected1))

isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
print(solution.findCircleNum2(isConnected2))