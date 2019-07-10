'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        # bottom-up, O(n) space
        res = triangle[-1]  # 最底一层
        for i in range(len(triangle)-2, -1, -1):  # 从倒数第2行开始
            for j in range(len(triangle[i])):  # 每行的每个数
                # res[j] = 从最底层到某行j位置的最小路径和
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
# Runtime: 40 ms, faster than 88.68% of Python3 online submissions for Triangle.
# Memory Usage: 13.5 MB, less than 85.65% of Python3 online submissions for Triangle.
