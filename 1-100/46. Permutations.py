'''
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)>1:
            return [[n]+aux for i,n in enumerate(nums) for aux in self.permute(nums[:i]+nums[i+1:])]
        else:
            return [nums]  # [[]], because 'for aux in'.
# Runtime: 44 ms, faster than 99.86% of Python3 online submissions for Permutations.

# 20190719
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 1:
            return [[n] + post for i, n in enumerate(nums)
                    for post in self.permute(nums[:i] + nums[i + 1:])]
        else:
            return [nums]
# Runtime: 52 ms, faster than 64.29% of Python3 online submissions for Permutations.
# Memory Usage: 13.2 MB, less than 71.03% of Python3 online submissions for Permutations.
