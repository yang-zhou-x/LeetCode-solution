class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row=len(matrix)
        small,large=matrix[0][0],matrix[-1][-1]+1

        while small<large:
            midd=(small+large)//2#二分法
            count=0
            col=len(matrix[0])-1
            for i in range(row):#遍历每一行
                while col>=0 and matrix[i][col]>midd:
                    col-=1
                count+=col+1#小于midd的个数
            if count<k:
                small=midd+1
            else:
                large=midd
        
        return small 

# Runtime: 52 ms, faster than 92.79% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 17.2 MB, less than 10.95% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
