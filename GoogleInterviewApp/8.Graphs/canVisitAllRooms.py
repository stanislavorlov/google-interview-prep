from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room):
            for neighbor in rooms[room]:
                if not neighbor in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = ({0})
        dfs(0)

        return len(rooms) == len(seen)