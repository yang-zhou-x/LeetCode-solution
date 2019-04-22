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
        maximum=big=small=nums[0]
        for n in nums[1:]:
            tmp1=max(n,n*big,n*small)
            tmp2=min(n,n*big,n*small)
            big=tmp1
            small=tmp2   # small记录为负数的情况
            maximum=max(maximum, big)
        return maximum
        
# Runtime: 48 ms, faster than 72.39% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 13.5 MB, less than 19.89% of Python3 online submissions for Maximum Product Subarray.
