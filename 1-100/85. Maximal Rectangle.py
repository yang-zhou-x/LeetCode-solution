'''
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

# 解法1
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)  # 实际上是m+1行n+1列的表格，首行全为0。这里简化了
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
# Runtime: 104 ms, faster than 58.76% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 13.8 MB, less than 86.80% of Python3 online submissions for Maximal Rectangle.

# 解法2
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0] * n  # left[i]是i处对应的左起点
        height = [0] * n  # height[i]是i处对应的高度
        right = [n] * n  # right[i]是i处对应的右端点
        ans = 0
        for i in range(m):  # 对每一行
            curr_left, curr_right = 0, n
            for j in range(n - 1, -1, -1):  # 从右向左
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n  # 为了不减小下一层的范围
                    curr_right = j  # 右边界（不包含）
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                    height[j] = height[j] + 1  # 上一层的高度 + 1
                else:
                    height[j] = 0
                    left[j] = 0  # 为了不减小下一层的范围
                    curr_left = j + 1  # 左边界（包含）
                ans = max(ans, height[j] * (right[j] - left[j]))
        return ans
# Runtime: 220 ms, faster than 71.05% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 14.8 MB, less than 6.25% of Python3 online submissions for Maximal Rectangle.
