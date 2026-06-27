# You are given an array of edges where edges[i] = [movieA, movieB]
# represents an undirected connection indicating two movies are similar.
# You are also given a dictionary ratings mapping movie titles to their float ratings.
# Given a start_movie and an integer n, return the top n highest-rated movies that are connected
# (directly or indirectly) to the start_movie.
# Do not include the start_movie itself in the recommendations.
# If there are fewer than n connected movies, return as many as possible.

import heapq
from collections import defaultdict, deque


class Solution:
    def getRecommendations(self, edges: list[list[str]], ratings: dict[str, float], start_movie: str, n: int) -> list[
        str]:
        # 1. Build the undirected graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. BFS Initialization
        queue = deque([start_movie])
        visited = {start_movie}

        # Min-heap to maintain the top 'n' movies.
        # Python's heapq is a min-heap, so the lowest rating stays at the top (index 0).
        min_heap = []

        # 3. Traverse the connected component
        while queue:
            curr = queue.popleft()

            # Evaluate the current movie (skip the start_movie itself)
            if curr != start_movie and curr in ratings:
                # Push a tuple of (rating, movie_name) into the heap
                heapq.heappush(min_heap, (ratings[curr], curr))

                # If the heap exceeds our limit 'n', pop the smallest rating out
                if len(min_heap) > n:
                    heapq.heappop(min_heap)

            # Add unvisited neighbors to the queue
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # 4. Extract results from the heap
        # The heap will pop from lowest rating to highest, so we need to reverse the result
        result = [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))]
        return result[::-1]

movies = [['A','B'], ['B', 'C'], ['A', 'D']]
raking = {'A': 9.8, 'B': 9.7, 'C': 10, 'D': 6}

print(Solution().getRecommendations(movies, raking, 'A', 2))