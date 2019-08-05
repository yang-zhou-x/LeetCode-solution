'''
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # 用于储存计算结果，避免重复计算

        def dfs(i, j): # 计算从matrix[i][j]出发的最长路径
            if not dp[i][j]:  # dp[i][j]为0时进行计算。已计算过的直接返回结果
                val = matrix[i][j]
                dp[i][j] = 1 + max(dfs(i - 1, j) if i and val < matrix[i - 1][j] else 0,
                                   dfs(i + 1, j) if i < m - 1 and val < matrix[i + 1][j] else 0,
                                   dfs(i, j - 1) if j and val < matrix[i][j - 1] else 0,
                                   dfs(i, j + 1) if j < n - 1 and val < matrix[i][j + 1] else 0)
            return dp[i][j]

        return max(dfs(i, j) for i in range(m) for j in range(n))
# Runtime: 216 ms, faster than 93.48% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 13.9 MB, less than 56.25% of Python3 online submissions for Longest Increasing Path in a Matrix.

# 20190805
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 用于储存计算结果，避免重复计算。每个格子代表从该位置出发的最大路径。
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and val < matrix[i-1][j] else 0,
                    dfs(i+1, j) if i + 1 < m and val < matrix[i+1][j] else 0,
                    dfs(i, j - 1) if j and val < matrix[i][j-1] else 0,
                    dfs(i, j+1) if j + 1 < n and val < matrix[i][j+1] else 0
                )
            return dp[i][j]
        return max(dfs(i, j) for i in range(m) for j in range(n))
# Runtime: 384 ms, faster than 96.21% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 14.3 MB, less than 58.33% of Python3 online submissions for Longest Increasing Path in a Matrix.
