class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        left=0
        for i in range(1,len(nums)):
            if nums[i]>nums[left]:
                left+=1
                nums[left]=nums[i]
        return left+1
    
# Runtime: 44 ms, faster than 99.03% of Python online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 12.6 MB, less than 39.90% of Python online submissions for Remove Duplicates from Sorted Array.
