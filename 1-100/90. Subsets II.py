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
        last = [[nums[0]]]  # 记录上一步加入ans的集合
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                last = [x + [nums[i]] for x in last]
                ans += last
            else:
                last = [x + [nums[i]] for x in ans]
                ans += last
        return ans
# Runtime: 40 ms, faster than 91.29% of Python3 online submissions for Subsets II.
# Memory Usage: 13.9 MB, less than 6.38% of Python3 online submissions for Subsets II.
