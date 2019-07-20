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
        res = []
        candidates.sort()
        def dfs(remain, path):
            if remain == 0:
                res.append(path)
                return 
            for item in candidates:
                if item > remain:  # early stop
                    break
                if path and item < path[-1]:  # keep unique
                    continue
                dfs(remain - item, path + [item])
        dfs(target, [])
        return res
# Runtime: 48 ms, faster than 99.89% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.9 MB, less than 5.05% of Python3 online submissions for Combination Sum.

# 加入索引的版本
class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        res = []
        candidates.sort()

        def dfs(remain, path, idx):
            if remain == 0:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], path + [candidates[i]], i)
        dfs(target, [], 0)
        return res
# Runtime: 56 ms, faster than 96.94% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.1 MB, less than 5.05% of Python3 online submissions for Combination Sum.
