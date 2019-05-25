'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines 
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Note: You may not slant the container and n is at least 2.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            ans = max(min(height[l], height[r])*(r-l), ans)
            # 从两侧向中间
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
# Runtime: 60 ms, faster than 85.66% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.5 MB, less than 39.17% of Python3 online submissions for Container With Most Water.
