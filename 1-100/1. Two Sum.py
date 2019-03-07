class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache={}
        for i,n in enumerate(nums):
            if target-n in cache:
                return [cache[target-n],i]
            cache[n]=i
            
