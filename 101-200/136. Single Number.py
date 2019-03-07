class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for n in nums:
            a^=n  # 按位操作符，异或
        return a
        
