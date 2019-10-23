'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
 
Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

from heapq import nlargest, nsmallest
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        elif len(nums) == 4:
            nums.sort()
            a1 = nums[1] * nums[2] * nums[3]
            a2 = nums[0] * nums[1] * nums[3]
            a3 = nums[0] * nums[1] * nums[2]
            return max(a1, a2, a3)
        else:
            positive = nlargest(3, nums)
            negative = nsmallest(2, nums)
            ans = max(negative[0]*negative[1]*positive[0], positive[0]*positive[1]*positive[2])
            return ans
# Runtime: 284 ms, faster than 99.40% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 14.9 MB, less than 6.67% of Python3 online submissions for Maximum Product of Three Numbers.
