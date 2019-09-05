'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > sum(x for x in range(10-k, 10)):
            return []
        ans = []

        def dfs(remain, path, start, t):
            if t == k:
                if remain == 0:
                    ans.append(path)
                return
            for i in range(start, 10):
                dfs(remain - i, path + [i], i + 1, t + 1)
        dfs(n, [], 1, 0)
        return ans
# Runtime: 40 ms, faster than 52.67% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Combination Sum III.


# 简化一下
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # k个数字，能取得的最大值为 10-k,9-k,...,9
        maxi = sum(x for x in range(10 - k, 10))
        if n > maxi:
            return []
        elif n == maxi:
            return [[x for x in range(10 - k, 10)]]
        ans = []

        def back_track(remain, path, start, idx):
            if idx == k:
                if remain == 0:
                    ans.append(path)
                    return
            # 满足要求时，第idx位上的数字范围
            for i in range(start, 11 + idx - k):
                if remain - i >= 0:
                    back_track(remain - i, path + [i], i + 1, idx + 1)
        back_track(n, [], 1, 0)
        return ans
# Runtime: 32 ms, faster than 95.83% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Combination Sum III.
