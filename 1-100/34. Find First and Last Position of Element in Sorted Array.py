'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.bs_left(nums, target)
        right = self.bs_right(nums, target)
        return (left, right) if left <= right else [-1, -1]

    def bs_left(self, nums, t):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if t <= nums[mid]:  # t=nums[mid]时，继续向左移动
                right = mid-1
            else:
                left = mid+1
        return left

    def bs_right(self, nums, t):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1  # t=nums[mid]时，继续向右移动
            if t >= nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return right
# Runtime: 20 ms, faster than 99.97% of Python online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 11.4 MB, less than 36.09% of Python online submissions for Find First and Last Position of Element in Sorted Array.
