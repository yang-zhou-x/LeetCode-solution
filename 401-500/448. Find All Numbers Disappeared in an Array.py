class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        aux=set(nums)
        return [x for x in range(1,len(nums)+1) if x not in aux]
        
