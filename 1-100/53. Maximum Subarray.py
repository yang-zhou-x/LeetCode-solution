class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[0]
        for n in nums:
            if ans[-1]>0:
                ans.append(ans[-1]+n)
            else:
                ans.append(n)
        return max(ans[1:])
        
# Runtime: 24 ms, faster than 98.34% of Python online submissions for Maximum Subarray.
# Memory Usage: 11.9 MB, less than 9.62% of Python online submissions for Maximum Subarray.


# 简化版本：
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)
        
# Runtime: 24 ms, faster than 98.34% of Python online submissions for Maximum Subarray.
# Memory Usage: 11.5 MB, less than 34.69% of Python online submissions for Maximum Subarray.
