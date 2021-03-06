'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        right, step = len(nums) - 1, 0
        start, end = 0, 0
        while end < right:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= right:  # 能跳到终点
                    return step
                maxend = max(maxend, i + nums[i])  # 能跳到的最远位置
            start, end = end + 1, maxend
        return step
# Runtime: 104 ms, faster than 91.55% of Python3 online submissions for Jump Game II.
# Memory Usage: 16.1 MB, less than 8.33% of Python3 online submissions for Jump Game II.
