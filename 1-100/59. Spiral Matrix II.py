'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        val = 1
        left, right, top, bot = 0, n - 1, 0, n - 1
        while left < right:
            for i in range(left, right):
                ans[top][i] = val
                val += 1
            top += 1
            for i in range(top - 1, bot):
                ans[i][right] = val
                val += 1
            right -= 1
            for i in range(right + 1, left, -1):
                ans[bot][i] = val
                val += 1
            bot -= 1
            for i in range(bot + 1, top - 1, -1):
                ans[i][left] = val
                val += 1
            left += 1
        if n % 2 == 1:  # n为奇数时
            ans[left][right] = val  # 最中心的格子
        return ans
# Runtime: 40 ms, faster than 55.42% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 13.8 MB, less than 5.94% of Python3 online submissions for Spiral Matrix II.
