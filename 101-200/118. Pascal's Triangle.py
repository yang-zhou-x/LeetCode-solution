class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[[1]*i for i in range(1,numRows+1)]
        for i in range(numRows):
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
        
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Pascal's Triangle.
# Memory Usage: 10.7 MB, less than 82.59% of Python online submissions for Pascal's Triangle.
 
