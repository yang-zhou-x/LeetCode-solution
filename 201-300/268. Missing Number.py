'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect = (1+len(nums))*len(nums) >> 1
        return expect-sum(nums)
# Runtime: 40 ms, faster than 97.05% of Python3 online submissions for Missing Number.
# Memory Usage: 14.2 MB, less than 34.23% of Python3 online submissions for Missing Number.
