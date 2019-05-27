'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, big * n, small * n), min(n, big * n, small * n)
            # small记录乘积为负数的情况
            maxi = max(maxi, big)
        return maxi
# Runtime: 40 ms, faster than 97.66% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 13.2 MB, less than 87.35% of Python3 online submissions for Maximum Product Subarray.
