'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: 
Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# 解法1：不使用除法
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)  # 不用除法
        p = 1
        for i in range(len(nums)):
            res[i] *= p
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res
# Runtime: 88 ms, faster than 99.94% of Python3 online submissions for Product of Array Except Self.

# 解法2：使用除法
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)
        prod = 1
        for i in nums:  # 使用除法
            if i:
                prod *= i
        if zeros == 1:
            return [0 if i else prod for i in nums]
        return [prod // i for i in nums]
