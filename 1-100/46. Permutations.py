class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)>1:
            return [[n]+aux for i,n in enumerate(nums) for aux in self.permute(nums[:i]+nums[i+1:])]
        else:
            return [nums]  # [[]], because 'for aux in'.
            
# Runtime: 44 ms, faster than 99.86% of Python3 online submissions for Permutations.
