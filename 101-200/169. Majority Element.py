class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=None
        count=0
        for n in nums:
            if count==0:
                ans=n
            count+=(1 if n==ans else -1)
        return ans
        
