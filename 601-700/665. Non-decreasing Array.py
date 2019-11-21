'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        start_idx = [0]  # 拆为若干个非降序序列，记录每个的起点
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                start_idx.append(i)
            if len(start_idx) > 2:
                return False
        if len(start_idx) == 2:
            if start_idx[1] == len(nums) - 1:  # 第2个序列长度为1
                return True
            if start_idx[1] - 1 == 0:  # 第1个序列长度为1
                return True
            if nums[start_idx[1] + 1] >= nums[start_idx[1] - 1]:
                return True
            if nums[start_idx[1] - 2] <= nums[start_idx[1]]:
                return True
            return False
        return True
# Runtime: 200 ms, faster than 95.49% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
