'''
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for n in nums:
            if n:
                nums[left] = n
                left += 1
        if left < len(nums):
            nums[left:] = [0]*(len(nums)-left)
# Runtime: 40 ms, faster than 99.45% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.7 MB, less than 5.32% of Python3 online submissions for Move Zeroes.
