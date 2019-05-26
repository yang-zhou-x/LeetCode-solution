'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# 动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 每个格子的值代表到达该格子的最小和
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == j == 0:  # 跳过dp[0][0]
                    continue
                dp_left = dp[i][j - 1] if j - 1 >= 0 else float('inf')  # 左侧
                dp_up = dp[i - 1][j] if i - 1 >= 0 else float('inf')  # 上侧
                # 当前值 = 左侧和上侧中的较小值 + 当前位置的值
                dp[i][j] = min(dp_left, dp_up) + grid[i][j]
        return dp[-1][-1]
# Runtime: 48 ms, faster than 99.13% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 14.9 MB, less than 7.98% of Python3 online submissions for Minimum Path Sum.
