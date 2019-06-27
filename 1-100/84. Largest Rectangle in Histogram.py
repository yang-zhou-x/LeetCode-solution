'''
Given n non-negative integers representing the histogram's bar height 
where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # fromLeft[i]为heights[i]左侧第一个小于heights[i]的位置
        fromLeft = [0] * len(heights)
        # fromRight[i]为heights[i]右侧第一个小于heights[i]的位置
        fromRight = [0] * len(heights)
        fromLeft[0] = -1
        fromRight[-1] = len(heights)
        for i in range(1, len(heights)):
            p = i - 1
            while p >= 0 and heights[i] <= heights[p]:
                p = fromLeft[p]  # 可以使复杂度从O(n^2)变为O(n)
            fromLeft[i] = p
        for i in range(len(heights) - 2, -1, -1):
            p = i + 1
            while p < len(heights) and heights[i] <= heights[p]:
                p = fromRight[p]  # 可以使复杂度从O(n^2)变为O(n)
            fromRight[i] = p
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (fromRight[i] - fromLeft[i] - 1))
        return ans
# Runtime: 68 ms, faster than 50.33% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 14.9 MB, less than 49.79% of Python3 online submissions for Largest Rectangle in Histogram.
