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
