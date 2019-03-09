class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev=0  # 相当于rob(nums[:-2])
        now=0  # 相当于rob(nums[:-1])
        for n in nums:
            tmp=prev
            prev=now
            now=max(tmp+n,now)   # 答案为 rob(nums[:-2])+nums[-1] 和 rob(nums[:-1]) 中较大的那个
        return now
        

# Runtime: 20 ms, faster than 84.00% of Python online submissions for House Robber.
# Memory Usage: 10.7 MB, less than 66.47% of Python online submissions for House Robber.
