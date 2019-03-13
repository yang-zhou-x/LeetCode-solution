class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[[]]
        for n in nums:
            ans+=[[n]+a for a in ans]
        
        return ans
        
# Runtime: 36 ms, faster than 99.87% of Python3 online submissions for Subsets.
