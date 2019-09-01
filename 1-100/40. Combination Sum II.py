'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        ans = []
        candidates.sort()

        def back_track(remain, path, idx):
            if remain == 0:
                ans.append(path)
            else:
                for i in range(idx, len(candidates)):
                    if candidates[i] > remain:
                        break  # early stop, 后面的数字都大于remain
                    # keep unique
                    if i > idx and candidates[i] == candidates[i-1]:
                        continue  # 重复数字只看第1个
                    back_track(remain - candidates[i],
                               path + [candidates[i]], i + 1)
        back_track(target, [], 0)
        return ans
# Runtime: 52 ms, faster than 86.89% of Python3 online submissions for Combination Sum II.
# Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for Combination Sum II.

