'''
Given a m x n matrix, if an element is 0, 
set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:  # 所有的0的位置
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i] = [0]*len(matrix[0])  # 行为0

        for j in col:
            for i in range(len(matrix)):
                if i not in row:
                    matrix[i][j] = 0  # 列为0
# Runtime: 88 ms, faster than 96.71% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 13.3 MB, less than 87.69% of Python3 online submissions for Set Matrix Zeroes.
