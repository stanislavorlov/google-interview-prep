# https://neetcode.io/problems/valid-sudoku

# You are given a a 9 x 9 Sudoku board board

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                cellValue = board[i][j]
                if cellValue == '.':
                    continue
                
                if cellValue in cols[i] or cellValue in rows[j] or cellValue in squares[str(i//3)+str(j//3)]:
                    return False
                else:
                    cols[i].add(cellValue)
                    rows[j].add(cellValue)
                    squares[str(i//3)+str(j//3)].add(cellValue)
        
        return True

solution = Solution()
board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board))    # True

board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board))    # False