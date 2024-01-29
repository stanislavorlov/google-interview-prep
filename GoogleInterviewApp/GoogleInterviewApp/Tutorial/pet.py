from collections import defaultdict
import collections


# strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

# res = defaultdict(list)
# for str in strings:
#     key = []
#     for ch in str:
#         key.append(ord(ch) - ord(str[0]) % 26)
#     res[tuple(key)].append(str)

# print(res)
# print(0 % 26)   #0
# print(1 % 26)   #1
# print(-1 % 26)   #25

def hash_code(i,j):
    return (i // 3, j // 3)

def valid_sudoke(board):
    hash_map = collections.defaultdict(list)
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            val = board[i][j]
            code = hash_code(i,j)
            if val == '.':
                continue
            if val not in hash_map[code]:
                hash_map[code].append(val)
            else:
                return False
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

print(valid_sudoke(board))

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(valid_sudoke(board))