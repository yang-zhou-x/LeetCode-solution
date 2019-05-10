'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = dp[idx - 1] + nums[idx] if dp[idx - 1] > 0 else nums[idx]
        return max(dp)
# Runtime: 36 ms, faster than 99.92% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.1 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.

# 简化版本：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
# Runtime: 40 ms, faster than 99.61% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.9 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
