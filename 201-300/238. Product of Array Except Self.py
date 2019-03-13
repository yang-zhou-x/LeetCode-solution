class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1 for _ in range(len(nums))]
        p=1
        for i in range(len(nums)):
            res[i]*=p
            p*=nums[i]
        
        p=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=p
            p*=nums[i]
        
        return res
        
# Runtime: 88 ms, faster than 99.94% of Python3 online submissions for Product of Array Except Self.
