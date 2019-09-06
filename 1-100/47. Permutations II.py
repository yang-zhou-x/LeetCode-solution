'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        ans = [[]]
        for n in nums:
            new_ans = []
            for part in ans:
                for i in range(len(part) + 1):
                    new_ans.append(part[:i] + [n] + part[i:])
                    if i < len(part) and part[i] == n:
                        break  #handles duplication
            ans = new_ans
        return ans
# Runtime: 56 ms, faster than 97.41% of Python3 online submissions for Permutations II.
# Memory Usage: 14 MB, less than 8.89% of Python3 online submissions for Permutations II.
