'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) 
of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [0] * len(nums)
        dp[0] = nums[:1]
        for i in range(1, len(nums)):
            local_maxi = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > len(local_maxi):
                    local_maxi = dp[j][:]
            dp[i] = local_maxi + [nums[i]]
        ans = []
        for sub in dp:
            if len(sub) > len(ans):
                ans = sub
        return ans
        # line 29-33:
        # return max(dp, key=lambda x: len(x))
# Runtime: 412 ms, faster than 64.27% of Python3 online submissions for Largest Divisible Subset.
# Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Largest Divisible Subset.
