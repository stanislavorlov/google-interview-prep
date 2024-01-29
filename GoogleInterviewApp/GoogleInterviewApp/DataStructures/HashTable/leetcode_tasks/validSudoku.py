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
            if board[i][j] == '.':
                continue
            if board[i][j] not in hash_map[hash_code(i,j)] and board[i][j] not in rows[i] and board[i][j] not in cols[j]:
                hash_map[hash_code(i,j)].add(board[i][j])
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
            else:
                return False

    return True

def isValidSudokuLeetcode(board: list[list[str]]) -> bool:
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudokuLeetcode(board))     #True

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(isValidSudokuLeetcode(board))     #False