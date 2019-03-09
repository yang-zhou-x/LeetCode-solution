class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        maxi=nums[0]
        for i,n in enumerate(nums):
            if n>maxi:
                maxi=n
                idx=i
        index=[x for x in range(len(nums)) if x!=idx]
        for i in index:
            try:
                if maxi/nums[i]<2:
                    return -1
            except ZeroDivisionError:
                pass
        return idx
        
# Runtime: 20 ms, faster than 97.98% of Python online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 10.7 MB, less than 70.00% of Python online submissions for Largest Number At Least Twice of Others.
