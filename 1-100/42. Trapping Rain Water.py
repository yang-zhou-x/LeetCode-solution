'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1  # 最左、最右端
        h1, h2 = 0, 0  # 记录左侧、右侧峰值
        ans = 0
        while l < r:
            if height[l] < height[r]:  # 选择较矮的一端
                if height[l] > h1:
                    h1 = height[l]  # 更新峰值
                else:
                    ans += h1-height[l]  # 累加结果
                l += 1
            else:
                if height[r] > h2:
                    h2 = height[r]  # 更新峰值
                else:
                    ans += h2-height[r]  # 累加结果
                r -= 1
        return ans
# Runtime: 40 ms, faster than 97.16% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.7 MB, less than 29.48% of Python3 online submissions for Trapping Rain Water.
