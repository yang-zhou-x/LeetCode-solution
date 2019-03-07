class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        aux=set()
        for n in nums:
            if n in aux:
                return True
            aux.add(n)
        return False
        
