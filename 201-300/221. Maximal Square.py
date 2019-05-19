'''
Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        for i in range(len(matrix)):
            matrix[i] = list(map(int, matrix[i]))  # 字符串 --> 数字
            row = matrix[i]
            for j, value in enumerate(row):
                if i*j*value:  # 不在上侧、左侧边界上，且当前位置的值不为0
                    row[j] = min(matrix[i-1][j-1], matrix[i-1][j],  # 动态规划，公式
                                 matrix[i][j-1]) + 1
        return max(map(max, matrix))**2
# Runtime: 80 ms, faster than 89.89% of Python3 online submissions for Maximal Square.
# Memory Usage: 14 MB, less than 33.58% of Python3 online submissions for Maximal Square.
