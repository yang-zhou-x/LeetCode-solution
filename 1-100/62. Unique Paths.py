'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

# 解法1：排列组合
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial as f
        return f(m + n - 2) // f(m - 1) // f(n - 1)
# Runtime: 36 ms, faster than 87.68% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.2 MB, less than 5.25% of Python3 online submissions for Unique Paths.

# 解法2：动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        # 实际上是m行n列的格子，这里重复使用了。格子内为到达该格子的路径数
        dp = [1] * n  # 第1行格子全部为1。实际上，第1列格子也全部为1。
        for i in range(1, m):  # 从第2行起的每1行
            for j in range(1, n):  # 依次向右
                # 当前格子路径数= 到达左侧格子的路径数 + 到达上侧格子的路径数
                dp[j] += dp[j - 1]
        return dp[-1]
# Runtime: 36 ms, faster than 89.14% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.1 MB, less than 62.84% of Python3 online submissions for Unique Paths.
