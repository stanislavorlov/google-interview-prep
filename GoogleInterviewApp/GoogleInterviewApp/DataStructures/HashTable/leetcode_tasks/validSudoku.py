# 9*9 Sudoku board
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'

import collections

def hash_code(i, j):
    return (i//3, j//3)

def isValidSudoku(board: list[list[str]]) -> bool:
    hash_map = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    for i in range(0,9):
        for j in range(0,9):
            val = board[i][j]
            if not val == '.':
                if val in hash_map[hash_code(i,j)] or val in rows[i] or val in cols[j]:
                    return False
                hash_map[hash_code(i,j)].add(val)
                rows[i].add(val)
                cols[j].add(val)

    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board)) #true