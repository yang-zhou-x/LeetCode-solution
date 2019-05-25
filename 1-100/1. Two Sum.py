'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, n in enumerate(nums):
            if target-n in cache:
                return [cache[target-n], i]
            cache[n] = i
# Runtime: 32 ms, faster than 99.28% of Python3 online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 41.10% of Python3 online submissions for Two Sum.
