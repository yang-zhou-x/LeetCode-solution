'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        right = len(nums)-2  # nums倒数第2个位置的索引
        dist = 1  # 距离
        while right > 0:  # 从右向左
            if nums[right] >= dist:
                dist = 1  # 能跳到，距离重置为1
            else:
                dist += 1  # 不能跳到，比较下一个位置，但距离要+1
            right -= 1
        return nums[0] >= dist  # 0位置能否跳到最近的能够跳到末尾的位置
# Runtime: 40 ms, faster than 97.40% of Python3 online submissions for Jump Game.
# Memory Usage: 14.6 MB, less than 32.38% of Python3 online submissions for Jump Game.
