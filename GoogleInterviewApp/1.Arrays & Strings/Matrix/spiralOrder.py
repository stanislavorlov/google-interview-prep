# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101   # max out of range value
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        current_direction = 0   # directions index
        change_direction = 0
        row, col = 0, 0
        result = [matrix[row][col]]
        matrix[row][col] = VISITED

        while change_direction < 2:
            while True:
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    break

                if matrix[next_row][next_col] == VISITED:
                    break

                change_direction = 0
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            current_direction = (current_direction + 1) % 4
            change_direction += 1

        return result

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))