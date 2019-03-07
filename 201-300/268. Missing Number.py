class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=(1+len(nums))*len(nums)//2
        return tot-sum(nums)

# Runtime: 24 ms, faster than 97.85% of Python online submissions for Missing Number.
# Memory Usage: 11.5 MB, less than 23.23% of Python online submissions for Missing Number.
 
