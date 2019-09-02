'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        ans = [[], [nums[0]]]
        new = [[nums[0]]]  # 最近加入的一批
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                new = [x + [nums[i]] for x in new]
            else:
                new = [x + [nums[i]] for x in ans]
            ans += new
        return ans
# Runtime: 36 ms, faster than 98.30% of Python3 online submissions for Subsets II.
# Memory Usage: 13.9 MB, less than 6.38% of Python3 online submissions for Subsets II.
