'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]*n for n in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return ans
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Pascal's Triangle.
# Memory Usage: 10.7 MB, less than 82.59% of Python online submissions for Pascal's Triangle.
