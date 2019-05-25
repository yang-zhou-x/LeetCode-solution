'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums)) + [0]
        n = len(nums)
        for i in range(len(nums)):  # 无用元素赋值为0
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # 使用hash来记录
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n
# Runtime: 36 ms, faster than 99.35% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for First Missing Positive.
