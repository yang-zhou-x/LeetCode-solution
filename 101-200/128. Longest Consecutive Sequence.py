'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # 去重
        longest = 0
        for n in nums:
            # nums可以看作由若干个连续片段组成(最短为1)，只考虑每段的开头
            if n-1 not in nums:  # 说明n是序列起点
                length = 1
                while n+1 in nums:  # 遍历该序列
                    n += 1
                    length += 1
                longest = max(longest, length)
        return longest
# Runtime: 36 ms, faster than 97.19% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 14.3 MB, less than 38.56% of Python3 online submissions for Longest Consecutive Sequence.
