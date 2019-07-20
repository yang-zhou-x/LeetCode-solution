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

# 先求出所有组合，再去重
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(remain, path, idx):
                if remain == 0:
                    res.append(path)
                    return
                for i in range(idx, len(candidates)):
                    if candidates[i] > remain:
                        break
                    dfs(remain - candidates[i], path + [candidates[i]], i + 1)
        dfs(target, [], 0)
        ans = []
        for r in res:
            if r not in ans:
                ans.append(r)
        return ans
# Runtime: 68 ms, faster than 60.39% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14 MB, less than 5.11% of Python3 online submissions for Combination Sum II.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(remain, path, idx):
                if remain == 0:
                    res.append(path)
                    return
                for i in range(idx, len(candidates)):
                    if candidates[i] > remain:
                        break
                    if i > idx and candidates[i] == candidates[i-1]:  # unique
                        continue  # 重复数字只看第1个
                    dfs(remain - candidates[i], path + [candidates[i]], i + 1)
        dfs(target, [], 0)
        return res
# Runtime: 48 ms, faster than 89.62% of Python3 online submissions for Combination Sum II.
# Memory Usage: 13.9 MB, less than 5.11% of Python3 online submissions for Combination Sum II.
