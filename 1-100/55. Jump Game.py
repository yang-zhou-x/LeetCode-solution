class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        right=len(nums)-2 # nums倒数第2个位置的索引
        dist=1
        while right>=0: # 从右向左
            if nums[right]>=dist:
                dist=1 # 能跳到，距离重置为1
            else:
                dist+=1 # 不能跳到，比较下一个位置，但距离要+1
            right-=1
        return nums[0]>=dist # 0位置能否跳到最近的能够跳到末尾的位置
# Runtime: 44 ms, faster than 90.88% of Python3 online submissions for Jump Game.
# Memory Usage: 14.5 MB, less than 5.28% of Python3 online submissions for Jump Game.
