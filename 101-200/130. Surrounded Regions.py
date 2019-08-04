'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on 
the border of the board are not flipped to 'X'. Any 'O' that is not on the border 
and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            m = len(board)
            n = len(board[0])
            border = [(0, i) for i in range(n)] + \
                [(m - 1, i) for i in range(n)] + \
                [(i, 0) for i in range(1, m)] + \
                [(i, n - 1) for i in range(1, m)]
            border = list(filter(lambda x: board[x[0]][x[1]] == 'O', border))
            while border:
                i, j = border.pop()
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                    board[i][j] = '.'
                    new = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    border.extend(new)
            for i in range(m):
                for j in range(n):
                    if board[i][j] == '.':
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
# Runtime: 160 ms, faster than 68.37% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 14.9 MB, less than 35.48% of Python3 online submissions for Surrounded Regions.
