class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):#每一行
            d=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in d:
                        return False
                    else:
                        d.add(board[i][j])
        
        for j in range(9):#每一列
            d=set()
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in d:
                        return False
                    else:
                        d.add(board[i][j])
        
        idx=[(i,j) for i in range(0,9,3) for j in range(0,9,3)]#起始位置
        for i,j in idx:#每个3x3的sub-box
            d=set()
            for ii,jj in itertools.product(range(i,i+3),range(j,j+3)):
                if board[ii][jj]!='.':
                    if board[ii][jj] in d:
                        return False
                    else:
                        d.add(board[ii][jj])
        return True
        
# Runtime: 52 ms, faster than 96.95% of Python3 online submissions for Valid Sudoku.
