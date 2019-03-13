class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row=[max(row) for row in grid]
        max_col=[max(col) for col in zip(*grid)]
        
        return sum(min(max_row[i],max_col[j])-val for i,row in enumerate(grid) for j,val in enumerate(row))
        
# Runtime: 44 ms, faster than 98.45% of Python3 online submissions for Max Increase to Keep City Skyline.
