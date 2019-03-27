class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row=set()
        col=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:  # 所有的0的位置
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i]=[0]*len(matrix[0])  # 行为0
            
        for j in col:
            for i in range(len(matrix)):
                if i not in row:
                    matrix[i][j]=0  # 列为0
                    
# Runtime: 84 ms, faster than 99.48% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 12.9 MB, less than 50.00% of Python3 online submissions for Set Matrix Zeroes.
