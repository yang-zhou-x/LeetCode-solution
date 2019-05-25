'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):  # 每一行
            d = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in d:
                        return False
                    else:
                        d.add(board[i][j])

        for j in range(9):  # 每一列
            d = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in d:
                        return False
                    else:
                        d.add(board[i][j])

        idx = ((i, j) for i in range(0, 9, 3) for j in range(0, 9, 3))  # 起始位置
        for i, j in idx:  # 每个3x3的sub-box
            d = set()
            for ii, jj in itertools.product(range(i, i+3), range(j, j+3)):
                if board[ii][jj] != '.':
                    if board[ii][jj] in d:
                        return False
                    else:
                        d.add(board[ii][jj])
        return True
# Runtime: 44 ms, faster than 98.44% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.4 MB, less than 5.12% of Python3 online submissions for Valid Sudoku.
