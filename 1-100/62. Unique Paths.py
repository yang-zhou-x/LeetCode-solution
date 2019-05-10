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

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial as f
        return f(m + n - 2) // f(m - 1) // f(n - 1)
# Runtime: 36 ms, faster than 87.68% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.2 MB, less than 5.25% of Python3 online submissions for Unique Paths.

# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        dp = [1] * n
        for i in range(1, m):  # 每1行
            for j in range(1, n):  # 依次向右
                dp[j] = dp[j - 1] + dp[j]  # = 到达左侧格子的路径数 + 到达上侧格子的路径数
        return dp[-1]
# Runtime: 36 ms, faster than 87.68% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.2 MB, less than 5.25% of Python3 online submissions for Unique Paths.
