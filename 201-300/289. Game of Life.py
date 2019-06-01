'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
Could you solve it in-place? 
Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. 
In principle, the board is infinite, which would cause problems 
when the active area encroaches the border of the array. How would you address these problems?
'''

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        ncol = len(board[0])
        for i, j in itertools.product(range(nrow), range(ncol)):
            sumNeighbors = sum(board[ii][jj] % 2
                               for ii in range(i-1, i+2)
                               for jj in range(j-1, j+2)
                               if 0 <= ii < nrow and 0 <= jj < ncol)\
                - board[i][j]  # 计算周围一圈的状态之和
            if board[i][j] == 0:  # die cell
                if sumNeighbors == 3:
                    board[i][j] = 2  # 用2记录。2%2==0
            else:  # live cell
                if sumNeighbors < 2 or sumNeighbors > 3:
                    board[i][j] = 3  # 用3记录。3%2==1
        for i, j in itertools.product(range(nrow), range(ncol)):
            if board[i][j] == 2:
                board[i][j] = 1  # 更新为1
            if board[i][j] == 3:
                board[i][j] = 0  # 更新为0
# Runtime: 20 ms, faster than 96.43% of Python online submissions for Game of Life.
# Memory Usage: 10.8 MB, less than 24.83% of Python online submissions for Game of Life.
