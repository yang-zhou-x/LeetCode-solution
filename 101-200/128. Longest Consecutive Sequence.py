class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums) #去重
        longest=0
        for n in nums:
            # nums可以看作由若干个连续片段组成(最短为1)，只考虑每段的开头
            if n-1 not in nums: # 说明n是序列起点
                curr=n
                length=1
                while curr+1 in nums: # 遍历该序列
                    curr+=1
                    length+=1
                longest=max(longest,length)
        return longest
# Runtime: 40 ms, faster than 89.78% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 14.3 MB, less than 5.31% of Python3 online submissions for Longest Consecutive Sequence.
