class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        for n in nums:
            if n!=0:
                nums[left]=n
                left+=1
        while left<len(nums):
            nums[left]=0
            left+=1
            
