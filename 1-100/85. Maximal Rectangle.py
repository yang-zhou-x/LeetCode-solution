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
        n = len(matrix[0])
        left = [0] * n
        height = [0] * n
        right = [n] * n
        ans = 0
        for i in range(len(matrix)):
            curr_left, curr_right = 0, n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curr_left)
                    height[j] = height[j] + 1
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_left = j + 1
                ans = max(ans, height[j] * (right[j] - left[j]))
        return ans
# Runtime: 100 ms, faster than 66.80% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 13.9 MB, less than 83.25% of Python3 online submissions for Maximal Rectangle.
