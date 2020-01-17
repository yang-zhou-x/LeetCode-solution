'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 
such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
(Each subgrid is contiguous).

Example 1:
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276
while this one is not:
384
519
762
In total, there is only one magic square inside the given grid.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0

        def distinct(i, j):
            nums = []
            for k in range(3):
                nums.extend(grid[i+k][j:j+3])
            check = set()
            for n in nums:
                if n in check or n == 0 or n > 9:
                    return False
                check.add(n)
            return True

        def row_sum(i, j):
            return sum(grid[i][j:j+3])

        def col_sum(i, j):
            return grid[i][j] + grid[i+1][j] + grid[i+2][j]

        m = len(grid)
        n = len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                if distinct(i, j) \
                    and row_sum(i, j) == row_sum(i+1, j) == row_sum(i+2, j) \
                    == col_sum(i, j) == col_sum(i, j+1) == col_sum(i, j+2) \
                        == (grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]):
                    ans += 1
        return ans
# Runtime: 36 ms, faster than 62.58% of Python3 online submissions for Magic Squares In Grid.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Magic Squares In Grid.
