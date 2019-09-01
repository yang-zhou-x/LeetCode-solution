'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def back_track(remain, path, idx):
            if remain == 0:
                ans.append(path)
            else:
                for i in range(idx, len(candidates)):
                    if candidates[i] > remain:
                        break  # early stop, 后面的数字都大于remain
                    back_track(remain - candidates[i], path + [candidates[i]], i)
        back_track(target, [], 0)
        return ans
# Runtime: 56 ms, faster than 96.94% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.1 MB, less than 5.05% of Python3 online submissions for Combination Sum.
