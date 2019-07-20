'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
  Integers in each row are sorted from left to right.
  The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i, j = 0, len(matrix[0]) - 1  # 从右上角开始搜索
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
# Runtime: 80 ms, faster than 8.99% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.7 MB, less than 5.09% of Python3 online submissions for Search a 2D Matrix.

# 也可以使用二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1
        while left <= right:
            mid = (left + right) >> 1
            i, j = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
# Runtime: 80 ms, faster than 8.99% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.8 MB, less than 5.09% of Python3 online submissions for Search a 2D Matrix.
