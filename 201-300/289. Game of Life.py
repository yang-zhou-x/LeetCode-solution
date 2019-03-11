class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        nrow=len(board)
        ncol=len(board[0])
        for i,j in itertools.product(range(nrow),range(ncol)):
            sumNeighbors=sum(board[ii][jj]%2 for ii in range(i-1,i+2) for jj in range(j-1,j+2) if 0<=ii<nrow and 0<=jj<ncol)-board[i][j]  # 计算周围一圈的状态之和
            if board[i][j]==0:  # die cell
                if sumNeighbors ==3:
                    board[i][j]=2 # 用2记录。2%2==0
            else:  # live cell
                if sumNeighbors <2 or sumNeighbors>3:
                        board[i][j]=3  # 用3记录。3%2==1
        
        for i,j in itertools.product(range(nrow),range(ncol)):
            if board[i][j]==2:
                board[i][j]=1  # 更新为1
            if board[i][j]==3:
                board[i][j]=0  # 更新为0
                
# Runtime: 20 ms, faster than 96.43% of Python online submissions for Game of Life.
# Memory Usage: 10.8 MB, less than 24.83% of Python online submissions for Game of Life.
